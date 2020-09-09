# -*- coding: utf-8 -*-
"""
부품찾기 - 이진탐색
"""


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    # mid위치의 값과 같으면 target return
    if array[mid] == target:
        return array[mid]

    # target보다 mid값이 크면
    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)  # 왼쪽 확인
    else:  # target보다 mid값이 작으면
        return binary_search(array, target, mid + 1, end)  # 오른쪽 확인


n = int(input())
n_array = list(map(int, input().split()))

m = int(input())
m_array = list(map(int, input().split()))

for i in m_array:
    result = binary_search(n_array, i, 0, n-1)
    if result is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')