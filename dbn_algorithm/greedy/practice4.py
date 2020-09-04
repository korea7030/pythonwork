# -*- coding: utf-8 -*-

"""
모험가 길드(p. 311)
 - N명의 모험가 정보가 주어지고, 공포도가 x인 모험가는 반드시 x명 이상으로 모험가를 구성
 - 최대 몇 개의 모험가 그룹을 만들 수 있느냐
"""
N = map(int, input())
data = list(map(int, input().split()))

result = 0
count = 0
data.sort()

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(count)
