N = int(input())

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split(' '))

    circle_count = int(input())
    outstacle = 0

    for j in range(circle_count):
        cx, cy, r = map(int, input().split(' '))

        d1 = (cx - x1) ** 2 + (cy - y1) ** 2  # 행성과 출발지점과의 거리
        d2 = (cx - x2) ** 2 + (cy - y2) ** 2  # 행성과 도착지점과의 거리

        if x1==x2 and y1==y2:
            outstacle = 0

        result1 = True if d1 > r*r else False
        result2 = True if d2 > r*r else False

        if result1 != result2:
            outstacle += 1


    print(outstacle)