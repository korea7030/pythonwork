# -*- coding: utf-8 -*-
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=False)
b.sort(reverse=True)

for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]  # 교체
    else:
        break

# A배열의 합
print(sum(a))