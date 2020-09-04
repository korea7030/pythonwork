# -*- coding: utf-8 -*-
"""
왕실의 나이트(p. 115)
"""
input_data = input()
row = int(input_data[1])  # 나이트의 row 좌표
column = int(ord(input_data[0])) - int(ord('a')) + 1  # 나이트의 column 좌표

# 나이트가 이동할 좌표
steps = [
    (-2, 1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

# 8가지 방향에 대하여 이동이 가능한지 체크
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
