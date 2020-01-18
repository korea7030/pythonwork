# -*- coding: utf-8 -*-


def is_promising(k, col):
    for row in range(1, k):
        # level - row = col - x[level]
        if col == x[row] or (abs(col - x[row]) == abs(k-row)):
            return False
    return True


def n_queens(k):
    """
    :param k: tree의 level값
    :return:
    """
    global count

    for col in range(1, N+1):
        if is_promising(k, col) is True:
            x[k] = col
            if k < N:
                n_queens(k+1)
            else:
                count += 1


if __name__ == '__main__':
    count = 0   # 구하고자 하는 방법
    N = int(input())    # 체스판의 크기
    x = [0] * (N+1)     # 체스판의 위치(동적 할당)
    n_queens(1)     # 1번째 row부터 각 row와 column별로 검사하기 위해 n_queens 호출
    print(count)
    print()
    print(x)