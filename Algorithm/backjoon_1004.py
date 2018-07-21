import math


N = int(input())
result = []

for i in range(N):
    x1,x2,y1,y2 = map(int, input().split(' '))

    circle_count = int(input())
    s1 = 0
    s2 = 0
    outstacle = 0

    for j in range(circle_count):
        cx,cy,r = map(int, input().split(' '))

        d1 = math.sqrt((cx - x1) ** 2 + (cy - y1) ** 2)  # 행성과 출발지점과의 거리
        d2 = math.sqrt((cx - x2) ** 2 + (cy - y2) ** 2)  # 행성과 도착지점과의 거리

        # 행성 중심과 출발/도착 지점과의 거리가 반지름보다 작으면
        # 그 행성에 속한 것으로 구분하여 해당 shell 값에 +1
        if d1 < r and d2 < r:
            s1 += 1
            s2 += 1
            outstacle += 1

        else:
            if d1 < r:
                s1 += 1
            if d2 < r:
                s2 += 1

    print(s1 + s2 - outstacle * 2)
