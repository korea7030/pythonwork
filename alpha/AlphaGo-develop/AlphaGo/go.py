import numpy as np

WHITE = -1
BLACK = +1
EMPTY = 0
PASS_MOVE = None

class GameState(object):
	"""State of a game of Go and some basic functions to interact with it
	"""

	def __init__(self, size=19):
		self.board = np.zeros((size, size))
		self.board.fill(EMPTY)
		self.size = size
		self.turns_played = 0
		self.current_player = BLACK
		self.ko = None
		self.history = []
		self.num_black_prisoners = 0
		self.num_white_prisoners = 0
		# `self.liberty_sets` is a 2D array with the same indexes as `board`
		# each entry points to a set of tuples - the liberties of a stone's
		# connected block. By caching liberties in this way, we can directly
		# optimize update functions (e.g. do_move) and in doing so indirectly
		# speed up any function that queries liberties
		self.liberty_sets = [[set() for _ in range(size)] for _ in range(size)]
		for x in range(size):
			for y in range(size):
				self.liberty_sets[x][y] = set(self._neighbors((x,y)))
		# separately cache the 2D numpy array of the _size_ of liberty sets
		# at each board position
		self.liberty_counts = np.zeros((size,size))
		self.liberty_counts.fill(-1)
		# initialize liberty_sets of empty board: the set of neighbors of each position
		# similarly to `liberty_sets`, `group_sets[x][y]` points to a set of tuples
		# containing all (x',y') pairs in the group connected to (x,y)
		self.group_sets = [[set() for _ in range(size)] for _ in range(size)]

	def get_group(self, position):
		"""Get the group of connected same-color stones to the given position

		Keyword arguments:
		position -- a tuple of (x, y)
		x being the column index of the starting position of the search
		y being the row index of the starting position of the search

		Return:
		a set of tuples consist of (x, y)s which are the same-color cluster 
		which contains the input single position. len(group) is size of the cluster, can be large. 
		"""
		(x, y) = position
		# given that this is already cached, it is a fast lookup
		return self.group_sets[x][y]

	def _on_board(self, position):
		"""simply return True iff position is within the bounds of [0, self.size)
		"""
		(x,y) = position
		return x >= 0 and y >= 0 and x < self.size and y < self.size

	def _neighbors(self, position):
		"""A private helper function that simply returns a list of positions neighboring
		the given (x,y) position. Basically it handles edges and corners.
		"""
		(x,y) = position
		return filter(self._on_board, [(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
	
	def _update_neighbors(self, position):
		"""A private helper function to update self.group_sets and self.liberty_sets 
		given that a stone was just played at `position`
		"""
		(x,y) = position

		merged_group = set()
		merged_group.add(position)
		merged_libs  = self.liberty_sets[x][y]
		for (nx, ny) in self._neighbors(position):
			# remove (x,y) from liberties of neighboring positions
			self.liberty_sets[nx][ny] -= set([position])
			# if neighbor was opponent, update group's liberties count
			# (current_player's groups will be updated below regardless)
			if self.board[nx][ny] == -self.current_player:
				new_liberty_count = len(self.liberty_sets[nx][ny])
				for (gx,gy) in self.group_sets[nx][ny]:
					self.liberty_counts[gx][gy] = new_liberty_count
			# MERGE group/liberty sets if neighbor is the same color
			# note: this automatically takes care of merging two separate
			# groups that just became connected through (x,y)
			elif self.board[x][y] == self.board[nx][ny]:
				merged_group |= self.group_sets[nx][ny]
				merged_libs  |= self.liberty_sets[nx][ny]

		# now that we have one big 'merged' set for groups and liberties, loop 
		# over every member of the same-color group to update them
		# Note: neighboring opponent groups are already updated in the previous loop
		count_merged_libs = len(merged_libs)
		for (gx,gy) in merged_group:
			self.group_sets[gx][gy] = merged_group
			self.liberty_sets[gx][gy] = merged_libs
			self.liberty_counts[gx][gy] = count_merged_libs

	def _remove_group(self, group):
		"""A private helper function to take a group off the board (due to capture),
		updating group sets and liberties along the way
		"""
		for (x,y) in group:
			self.board[x,y] = EMPTY
		for (x,y) in group:
			# clear group_sets for all positions in 'group'
			self.group_sets[x][y] = set()
			self.liberty_sets[x][y] = set()
			self.liberty_counts[x][y] = 0
			for (nx,ny) in self._neighbors((x,y)):
				if self.board[nx,ny] == EMPTY:
					# add empty neighbors of (x,y) to its liberties
					self.liberty_sets[x][y].add((nx,ny))
					self.liberty_counts[x][y] += 1
				else:
					# add (x,y) to the liberties of its nonempty neighbors
					self.liberty_sets[nx][ny].add((x,y))
					self.liberty_counts[nx][ny] += 1

	def copy(self):
		"""get a copy of this Game state
		"""
		other = GameState(self.size)
		other.board = self.board.copy()
		other.turns_played = self.turns_played
		other.current_player = self.current_player
		other.ko = self.ko
		other.history = self.history
		other.num_black_prisoners = self.num_black_prisoners
		other.num_white_prisoners = self.num_white_prisoners

		# update liberty and group sets. Note: calling set(a) on another set
		# copies the entries (any iterable as an argument would work so
		# set(list(a)) is unnecessary)
		for x in range(self.size):
			for y in range(self.size):
				other.group_sets[x][y] = set(self.group_sets[x][y])
				other.liberty_sets[x][y] = set(self.liberty_sets[x][y])
		other.liberty_counts = self.liberty_counts.copy()
		return other

	def is_suicide(self, action):
		"""return true if having current_player play at <action> would be suicide
		"""
		(x,y) = action
		num_liberties_here = len(self.liberty_sets[x][y])
		if num_liberties_here == 0:
			# no liberties here 'immediately'
			# but this may still connect to another group of the same color
			for (nx,ny) in self._neighbors(action):
				# check if we're saved by attaching to a friendly group that has
				# liberties elsewhere
				is_friendly_group = self.board[nx,ny] == self.current_player
				group_has_other_liberties = len(self.liberty_sets[nx][ny] - set([action])) > 0
				if is_friendly_group and group_has_other_liberties:
					return False
				# check if we're killing an unfriendly group
				is_enemy_group = self.board[nx,ny] == -self.current_player
				if is_enemy_group and (not group_has_other_liberties):
					return False
			# checked all the neighbors, and it doesn't look good.
			return True
		return False

	def is_legal(self, action):
		"""determine if the given action (x,y tuple) is a legal move

		note: we only check ko, not superko at this point (TODO?)
		"""
		# passing move
		if action is PASS_MOVE:
			return True
		(x,y) = action
		empty = self.board[x][y] == EMPTY
		suicide = self.is_suicide(action)
		ko = action == self.ko
		return self._on_board(action) and (not suicide) and (not ko) and empty 

	def is_eye(self, position, owner):
		"""returns whether the position is empty and is surrounded by all stones of 'owner'
		"""
		(x,y) = position
		if self.board[x,y] != EMPTY:
			return False

		for (nx,ny) in self._neighbors(position):
			if self.board[nx,ny] != owner:
					return False
		return True

	def get_legal_moves(self):
		moves = []
		for x in range(self.size):
			for y in range(self.size):
				if self.is_legal((x,y)):
					moves.append((x,y))
		return moves

	def do_move(self, action):
		"""Play current_player's color at (x,y)

		If it is a legal move, current_player switches to the other player
		If not, an IllegalMove exception is raised
		"""
		if self.is_legal(action):
			# reset ko
			self.ko = None
			if action is not PASS_MOVE:
				(x,y) = action
				self.board[x][y] = self.current_player
				self._update_neighbors(action)
				
				# check neighboring groups' liberties for captures
				for (nx, ny) in self._neighbors(action):
					if self.board[nx,ny] == -self.current_player and len(self.liberty_sets[nx][ny]) == 0:
						# capture occurred!
						captured_group = self.group_sets[nx][ny]
						num_captured = len(captured_group)
						self._remove_group(captured_group)
						if self.current_player == BLACK:
							self.num_white_prisoners += num_captured
						else:
							self.num_black_prisoners += num_captured
						# check for ko
						if num_captured == 1:
							# it is a ko iff, were the opponent to play at the captured position,
							# it would recapture (x,y) only
							# (a bigger group containing xy may be captured - this is 'snapback')
							would_recapture = len(self.liberty_sets[x][y]) == 1
							recapture_size_is_1 = len(self.group_sets[x][y]) == 1
							if would_recapture and recapture_size_is_1:
								# note: (nx,ny) is the stone that was captured
								self.ko = (nx,ny)
			# next turn
			self.current_player = -self.current_player
			self.turns_played += 1
			self.history.append(action)
		else:
			raise IllegalMove(str(action))

	def symmetries(self):
		"""returns a list of 8 GameState objects:
		all reflections and rotations of the current board

		does not check for duplicates
		"""

		# we use numpy's built-in array symmetry routines for self.board.
		# but for all xy pairs (i.e. self.ko and self.history), we need to
		# know how to rotate a tuple (x,y) into (new_x, new_y)
		xy_symmetry_functions = {
			"noop":   lambda (x,y): (x, y),
			"rot90":  lambda (x,y): (y, self.size-x),
			"rot180": lambda (x,y): (self.size-x, self.size-y),
			"rot270": lambda (x,y): (self.size-y, x),
			"mirror-lr": lambda (x,y): (self.size-x, y),
			"mirror-ud": lambda (x,y): (x, self.size-y),
			"mirror-\\": lambda (x,y): (y, x),
			"mirror-/":  lambda (x,y): (self.size-y, self.size-x)
		}

		def update_ko_history(copy, name):
			if copy.ko is not None:
				copy.ko = xy_symmetry_functions[name](copy.ko)
			copy.history = [xy_symmetry_functions[name](a) if a is not PASS_MOVE else PASS_MOVE for a in copy.history]

		copies = [self.copy() for i in range(8)]
		# copies[0] is the original.
		# rotate CCW 90
		copies[1].board = np.rot90(self.board,1)
		update_ko_history(copies[1], "rot90")
		# rotate 180
		copies[2].board = np.rot90(self.board,2)
		update_ko_history(copies[2], "rot180")
		# rotate CCW 270
		copies[3].board = np.rot90(self.board,3)
		update_ko_history(copies[3], "rot270")
		# mirror left-right
		copies[4].board = np.fliplr(self.board)
		update_ko_history(copies[4], "mirror-lr")
		# mirror up-down
		copies[5].board = np.flipud(self.board)
		update_ko_history(copies[5], "mirror-ud")
		# mirror \ diagonal
		copies[6].board = np.transpose(self.board)
		update_ko_history(copies[6], "mirror-\\")
		# mirror / diagonal (equivalently: rotate 90 CCW then flip LR)
		copies[7].board = np.fliplr(copies[1].board)
		update_ko_history(copies[7], "mirror-/")
		return copies

	def from_sgf(self, sgf_string):
		raise NotImplementedError()

	def to_sgf(self, sgf_string):
		raise NotImplementedError()


class IllegalMove(Exception):
	pass