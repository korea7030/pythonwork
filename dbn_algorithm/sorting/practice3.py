# -*- coding: utf-8 -*-
"""
퀵정렬(p.168 ~ 169)
"""
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = pivot + 1
    right = end

    while left <= right:
        # pivot보다 큰 데이터
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # pivot보다 작은 데이터
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈렸다면 right 위치와 pivot 바꾸기
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]

    # 분할 후 왼쪽, 오른쪽 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def quick_sort_py(array):
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗 첫번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # pivot보다 작으면 왼쪽 리스트
    right_side = [x for x in tail if x > pivot]  # pivot보다 크면 오른쪽 리스트

    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)


def quick_sort_py2(array):
    """
    tail을 정하지 않은 경우
    :param array:
    :return:
    """
    if len(array) <= 1:
        return array

    import math
    pivot = array[math.floor(len(array) / 2)]  # pivot 설정(중앙값)

    left_side = [array[i] for i in range(len(array)) if array[i] < pivot]
    right_side = [array[i] for i in range(len(array)) if array[i] > pivot]

    return quick_sort_py2(left_side) + [pivot] + quick_sort_py2(right_side)


quick_sort(array, 0, len(array)-1)
print(quick_sort_py(array))
print(quick_sort_py2(array))