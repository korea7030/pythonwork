# -*- config: utf-8 -*-
# MAX-HEAPIFY


def heapify(arr, index, heap_size):
    # 완전이진트리는 배열 하나로 트리 구현가능
    largest = index
    left = index * 2 + 1
    right = index * 2 + 2

    # 왼쪽 자식이 현재 요소보다 크면 인덱스 교체
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 현재 요소보다 크면 인덱스 교체
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # 교체된적이 있다면 교체된 index와 largest 요소값 교체
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        # 변경되었다면 변경된 부분을 중심으로 heapify
        heapify(arr, largest, heap_size)


def heap_sort(arr):
    n = len(arr)

    # 최초힙(최대값이 맨앞으로 이동)
    # 트리의 절반부터 거꾸로 올라가며 heapify하는 것이 효율적
    # 이진트리의 성질에 의해 모든 요소값을 서로 한번씩 비교할 수 있음 : O(n)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)

    print('initialize heap : ' + str(arr))

    # 한번 구성한 heap을 정렬
    # 가장 큰 값(루트)를 가장 끝으로 이동한 후 힙 생성
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr


"""
parent index return
"""


def parent(index):
    return index // 2


"""
max_heap insert
"""


def max_heap_insert(arr, node):
    arr.append(node)
    heap_size = len(arr) - 1
    i = heap_size

    while i > 1:
        p = parent(i)
        if arr[i] < arr[p]:
            tmp = arr[i]
            arr[i] = arr[p]
            arr[p] = tmp
            i = p
        else:
            break

    heap_sort(arr)

    return arr


def extract_max(arr, heap_size):
    if heap_size < 1:
        return

    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))

    max = arr.pop(0)
    arr[0] = arr[heap_size]

    return max


if __name__ == '__main__':
    data = [61, 324, 21, 56, 243, 6, 1, 634, 43, 3, 52]
    print(heap_sort(data))
    print(extract_max(data, 4))
    # print(max_heap_insert(data, 555))
