# -*- coding: utf-8 -*-
"""
위에서 아래로(p.178)
"""
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array)

for i in array:
    print(i, end=' ')
