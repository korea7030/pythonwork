# -*- coding: utf-8 -*-
"""
시분초 시간계산(p. 113)
00시00분00초 ~ N시59분59초 까지에서 3이 몇번 나오는지
"""
h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)