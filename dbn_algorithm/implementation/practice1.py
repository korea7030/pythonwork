# -*- cofing: utf-8 -*-
"""
상하좌우 이동 문제(p. 110)
 - 방향을 숫자로 표시
"""
N = int(input())
direction = input().split()

# L, R, U, D 를 숫자로
dx = [0, 0, -1, -1]
dy = [-1, -1, 0, 0]

# 초기시작점
x,y = 1, 1

move_direction = ['L', 'R', 'U', 'D']

for plan in direction:
    for i in range(len(move_direction)):
        # plan과 direction 체크 후 좌표값 update
        if plan == direction[i]:
            nx = x + dx[i]  # L, R
            ny = y + dy[i]  # U, D

    if nx < 1 or ny < 1:
        continue
    x, y = nx, ny
print(x, y)
