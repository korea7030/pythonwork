# -*- coding: utf-8 -*-
'''
병합정렬
 : 특정 수가 나열된 배열을 정렬하기 위해 분할하여 정렬 수행
 : 우선 쪼갤 수 없는 단위까지 분할 수행
 : 분할 후 나온 왼쪽 배열과 오른쪽 배열의 크기를 비교하여 정렬
 시간복잡도 : O(n*log(n))
  분할 시 log(n) >> 자료의 개수가 8개인경우 2^2 < 호출레벨 =< 2^3
  비교후 병합 시 n(원소의 개수)
'''
def divie_arr(arr):
    if len(arr) > 1:
        # 가운데를 기준으로 분할
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        # 가운데를 기준으로 분할 후 각각의 배열에 대해 재분할
        l_div = divie_arr(left)
        r_div = divie_arr(right)

        # 분할된 배열에 대해 정렬 후 병합
        return merge(l_div, r_div)
    else:
        return arr

## 정렬 후 병합
def merge(left, right):
    i=0
    j=0
    merge_arr = []

    # 양쪽 배열에서 크기를 비교하여 작은 수가 나온 배열의 요소를 병합배열에 추가
    while (i<len(left)) & (j<len(right)):
        if left[i] < right[j]:
            merge_arr.append(left[i])
            i+=1
        else:
            merge_arr.eppend(right[j])
            j+=1

    # 두 배열 비교 후 남은 값을 정렬(left)
    while (i<len(left)):
        merge_arr.append(left[i])
        i+=1

    # 두 배열 비교 후 남은 값을 정렬(right)
    while (j<len(right)):
        merge_arr.append(right[j])
        j+=1

    return merge_arr

if __name__=="__main__":
    arr = [1,4,5,7,8,9,10,20]
    print(divie_arr(arr))
