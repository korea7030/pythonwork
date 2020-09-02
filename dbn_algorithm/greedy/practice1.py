# -*- coding: utf-8 -*-

"""
큰 수의 법칙
"""
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[N-1]
second = data[N-2]
result = 0

# 가장 큰 수가 더해지는 횟수 계산
count = int(M / (K+1)) * K
count += M % (K+1)

result += count * first  # 가장 큰수
result += (M-count) * second  # 두번째로 큰 수

print(result)
