# -*- coding: utf-8 -*-
"""
계수 정렬(Count Sort, p.174)
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 5, 2]

c_array = [0] * (max(array) + 1)

for i in array:
    c_array[i] += 1  # 각 데이터에 해당하는 인덱스값 업데이트

for i in range(len(c_array)):  # 리스트에 저장된 정렬 정보 확인
    for j in range(c_array[i]):
        print(i, end=' ')
