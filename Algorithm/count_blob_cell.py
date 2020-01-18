class CountBlob:
    def get_blob_count(self, x, y):
        # print("ddd : " +str(cell[x][y]))
        if (x < 0 | x > N | y < 0 | y > N):
            return 0
        elif cell[x][y] != IMAGE_COLOUR:
            return 0
        else:
            cell[x][y] = BLOCKED_COLOUR
            return self.get_blob_count(x, y+1) + self.get_blob_count(x + 1, y + 1) + \
                        self.get_blob_count(x + 1, y) + self.get_blob_count(x + 1, y - 1) + \
                        self.get_blob_count(x, y-1) + self.get_blob_count(x - 1, y - 1) + \
                        self.get_blob_count(x - 1, y) + self.get_blob_count(x - 1, y + 1) +1


if __name__ == '__main__':
    # N x N 행렬, 입력값(x,y), image color, blocked color
    N = 8
    CELL_COUNT = 0
    IMAGE_COLOUR = 1
    BLOCKED_COLOUR = 2
    cell = [[1, 0, 0, 0, 0, 0, 0, 1],
      [0, 1, 1, 0, 0, 1, 0, 0],
      [1, 1, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 1, 0, 0],
      [0, 1, 0, 1, 0, 1, 0, 0],
      [0, 1, 0, 1, 0, 1, 0, 0],
      [1, 0, 0, 0, 1, 0, 0, 1],
      [0, 1, 1, 0, 0, 1, 1, 1]]

    print(cell[2][4])
    exp = CountBlob()
    res = exp.get_blob_count(3, 5)
    print(res)