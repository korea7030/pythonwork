# -*- coding: utf-8 -*-
"""
볼링공 고르기
"""


def my_solution(N, M, data):
    result = 0

    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] != data[j]:
                result += 1

    print(result)


def book_solution(N, M, data):
    array = [0] * 11

    for x in data:
        array[x] += 1

    result = 0
    for i in range(1, M+1):
        N -= array[i]
        result += array[i] * N

    print(result)


if __name__ == '__main__':
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    my_solution(N, M, data)
    book_solution(N, M, data)
