# -*- coding: utf-8 -*-
"""
1이 될때까지(p. 99)
어떤 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 수행. 단 두번째 연산은 N이 K로 나누어 떨어질때만 선택
  1. N에서 1을 뺀다
  2. N을 K로 나눈다
"""
import time


def n_to_one_1(N, K):
    """
    내가 짠 것
    :param N:
    :param K:
    :return:
    """
    start = time.time()
    count = 0

    while N != 1:
        if N % K == 0:
            N = int(N / K)
            count += 1
        else:
            N = N - 1
            count += 1

    print(count)
    end = time.time()
    print('time : {}'.format(end - start))


def n_to_one_2(N, K):
    """
    책 예제1
    :param N:
    :param K:
    :return:
    """
    start = time.time()
    count = 0

    # N을 K로 나누기(K보다 클 때까지)
    while N >= K:
        while N % K != 0:
            N -= 1
            count += 1

        N //= K
        count += 1

    # N이 K보다 작고 1보다 큰 경우(1을 빼기)
    while N > 1:
        N -= 1
        count += 1

    print(count)
    end = time.time()
    print('time : {}'.format(end - start))


def n_to_one_3(N, K):
    start = time.time()
    count = 0

    while True:
        # N == K가 될때까지 1씩 빼주기
        target = (N // K) * K
        count += (N - target)
        N = target

        # N < K 일 때 반복문 탈출
        if N < K:
            break

        count += 1
        N //= K

    # 마지막으로 남은 수에 대하여 1 빼기
    count += (N-1)

    print(count)
    end = time.time()
    print('time : {}'.format(end - start))


if __name__ == '__main__':
    N, K = map(int, input().split())
    n_to_one_1(N, K)
    n_to_one_2(N, K)
    n_to_one_3(N, K)
