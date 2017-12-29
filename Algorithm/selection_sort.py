# -*- coding: utf-8 -*-
'''
선택정렬
 : 나열된 숫자에서 작은수를 선택해서 차례대로 정렬
 방법
  1) 배열의 첫번째 index 값을 선택해서 전체 비교후 정렬
  2) 이후 첫번째 index를 제외한 나머지 요소로 정렬 진행
 시간복잡도 : O(n^2)
'''


def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp

    return arr


if __name__ == "__main__":
    arr = [1, 6, 3, 9, 7, 8, 4, 30, 20, 10]
    print(selection_sort(arr))
