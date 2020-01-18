'''
merge sort
 - 시간복잡도
 best : O(nlog(n)), worst : O(nlog(n)log(n))
'''


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:  # left, right 둘다 있는 경우
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:  # left만 있는 경우
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:  # right만 있는 경우
            result.append(right[0])
            right = right[1:]
    return result


def merge_sort(list):
    if len(list) <= 1:
        return list

    # 데이터를 절반으로 나눔
    mid = len(list) // 2
    left_list = list[:mid]
    right_list = list[mid:]
    # 각각의 배열을 정렬
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    # 최종 정렬(merge)
    return merge(left_list, right_list)


if __name__ == '__main__':
    lst = [14, 7, 3, 12, 9, 11, 6, 2]
    res = merge_sort(lst)
    print(res)
