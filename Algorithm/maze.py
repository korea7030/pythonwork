class Maze:
    def find_mazh_path(self, x, y):
        # 미로 범위 밖인지 여부 체크 false
        if (x < 0 or y < 0 or x >= N or y >= N):
            return False
        # 좌표가 이미 방문된 곳인거나 출구인 경우 -> PATHWAY_COLOUR가 아닌 경우 false
        elif (maze[x][y] != PATHWAY_COLOUR):
            return False
        # 출구 좌표인 경우
        elif (x == N-1 and y == N-1):
            return False
        # 위치 방문, 인접하 4 위치를 findPath 호출해서 경로가 있으면 true
        else:
            maze[x][y] = PATH_COLOUR
            if (self.find_mazh_path(x-1, y) or self.find_mazh_path(x, y-1) or
                    self.find_mazh_path(x+1, y) or self.find_mazh_path(x, y+1)):
                return True
            maze[x][y] = BLOCKED_COLOUR
            return False

    def print_maze(self, maze):
        for x in maze:
            print(x, end=' ')
            print()


if __name__ == '__main__':
    N = 8
    maze = [[0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 0, 0, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0, 1, 0, 0]]

    PATHWAY_COLOUR = 0  # white
    WALL_COLOUR = 1  # blue
    BLOCKED_COLOUR = 2  # red (visited이며 출구까지 경로상에 있지 않음이 밝혀진 cell)
    PATH_COLOUR = 3  # green (visited이며 아직 출구로 가는 경로가 될 가능성이 있는 cell)

    s = Maze()
    # s.print_maze(maze)
    s.find_mazh_path(0,0)
    s.print_maze(maze)