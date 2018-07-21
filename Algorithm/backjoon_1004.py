import math

N = int(input())

for i in range(N):
    x1, x2, y1, y2 = map(int, input().split(' '))

    circle_count = int(input())
    outstacle = 0

    for j in range(circle_count):
        cx, cy, r = map(int, input().split(' '))

        d1 = math.sqrt((cx - x1) ** 2 + (cy - y1) ** 2)  # 행성과 출발지점과의 거리
        d2 = math.sqrt((cx - x2) ** 2 + (cy - y2) ** 2)  # 행성과 도착지점과의 거리

        if d1 < r:
            outstacle += 1

        if d2 < r:
            outstacle += 1

    print(outstacle)