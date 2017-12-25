# -*- coding: utf-8 -*-
'''
쉘정렬
 : 일정 간격 떨어진 원소들끼리 먼저 정렬시키고 전체를 수행
 : 삽입정렬의 업그레이드 버전
'''
def shell_sort(arr):
    gap = len(arr) // 2

    while(gap > 0):
        for i in range(gap):
            for j in range(i+gap, len(arr), gap):
                cur_val = arr[j]
                position = j

                # gpa 번째 index를 기준으로 gap 만큼 뺀 위치의 값과 비교
                # 앞의 값이 크다면 swap 진행
                while position >= gap and arr[position-gap] > cur_val:
                    arr[position] = arr[position-gap]
                    position = position-gap

                arr[position] = cur_val
                # print(arr[position])

            print("gap = "+str(gap)+" cur_val : "+str(cur_val)+" position : "+str(position)+" step : "+str(i+1)+" : "+str(arr))
        gap = gap//2
    return arr

if __name__=="__main__":
    arr = [5,3,2,7,10,8,30,9,50,1]
    print(shell_sort(arr))
