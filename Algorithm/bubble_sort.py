# -*- coding: utf-8 -*-
'''
버블정렬
 : 첫번째 index부터 차례차례로 비교해보며 정렬
 시간복잡도 : O(n^2)
'''
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp


    return arr

if __name__=="__main__":
    arr = [1,8,6,7,5,30,35,10]
    print(bubble_sort(arr))
