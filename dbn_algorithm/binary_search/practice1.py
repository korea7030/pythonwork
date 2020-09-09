# -*- coding: utf-8 -*-
"""
이진 탐색
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
        return binary_search(array, target, start, mid-1)  # 왼쪽 확인
    else:  # target보다 mid값이 작으면
        return binary_search(array, target, mid+1, end)  # 오른쪽 확인


if __name__ == '__main__':
    array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    print(binary_search(array, 4, 0, len(array)-1))