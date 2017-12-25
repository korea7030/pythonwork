# -*- coding: utf-8 -*-
'''
삽입정렬
 : 1~N 사이의 인덱스에서 점진적으로 정렬 범위를 넓혀 나감.
'''
def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                tmp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = tmp
            else:
                break

    return arr

if __name__=="__main__":
    arr = [3,1,9,7,8,15,2,30]
    print(insertion_sort(arr))
