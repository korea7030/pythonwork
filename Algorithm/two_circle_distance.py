import math

'''
두 원의 위치관계 - 두 점 에서 만나는 경우 
r1 - r2 < distance < r1 + r2

두 원의 위치관계 - 한 점에서 만나는 경우, 내접, 외접
r1 + r2 = distance(외접)
r1 - r2 = distance(내접)

두 원의 위치관계 - 만나지 않는 경우, 외부에 있을 때, 내부에 있을 때, 동심원
r1 + r2 < distance (외부에 있을 때)
distance < r1 - r2 (내부에 있을 때)
d = 0, r1 != r2 (동심원) 
'''
def find_num(N):
    x1, y1, r1, x2, y2, r2 = map(int, N.split(' '))

    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

    if distance == 0:
        if r1 == r2:
            print('-1')
        else:
            print('0')

    elif distance < abs(r1-r2):
        print("0")
    elif distance > r1+r2:
        print("0")
    elif distance == r1+r2:
        print("1")
    elif distance == abs(r1-r2):
        print("1")
    elif abs(r1-r2) < distance and distance < r1+r2:
        print("2")


trials = int(input())

for i in range(trials):
    N = input()
    find_num(N)