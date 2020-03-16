'''
    binary search
    시간 복잡도 : O(logN)
    정렬된 자료를 반으로 나누어 탐색
    ** 자료는 항상 정렬되어 있어야 함
    dynamic programming, recursion의 단골
'''


def binary_search_v1(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1

    return None


def binary_search_v2(target, start, end, data):
    data.sort()
    if start > end:
        return None

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] <= target:
            start = mid + 1
            return binary_search_v2(target, start, end, data)
        else:
            end = mid - 1
            return binary_search_v2(target, start, end, data)


if __name__ == '__main__':
    data = [i ** 2 for i in range(11)]
    mid = binary_search_v1(9, data)

    if mid:
        print(data[mid])
    else:
        print("no")

    mid2 = binary_search_v2(9, 0, 10, data)
    print(data[mid2])
