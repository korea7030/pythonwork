# -*- coding: utf-8 -*-
"""
부품 찾기 - set() 사용
"""
n = int(input())

array = set(map(int, input().split()))

m = int(input())

x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
