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
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)


if __name__ == '__main__':
    lst = [14, 7, 3, 12, 9, 11, 6, 2]
    res = merge_sort(lst)
    print(res)
