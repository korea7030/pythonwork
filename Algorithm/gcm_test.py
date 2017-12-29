'''
유클리드 호제법을 통한 최대공약수 & 최소공배수
'''


def gcm(x, y):
    res = x % y

    # res 가 0일때 까지 진행
    while(res):
        # y를 x에 대입
        # x를 y로 나눈 나머지를 y에 대입
        x = y
        y = res
        res = x % y

    return y


def lcm(x, y):
    lcm = (x * y) // gcm(x, y)
    return lcm


if __name__ == "__main__":
    print(gcm(20, 12))
    print(lcm(20, 12))
