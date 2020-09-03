# -*- coding: utf-8 -*-
"""
만들수 없는 금액
 - N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최소 금액을 구하라
   정렬 + 그리디 알고리즘
"""
N = map(int, input())
data = list(map(int, input().split()))
target = 1

data.sort()

for i in data:
    if target < i:
        break
    target += i

print(target)