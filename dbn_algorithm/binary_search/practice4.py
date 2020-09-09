# -*- coding: utf-8 -*-
"""
떡볶이 떡 만들기
"""

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid

    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 탐색)
    if total < m:
        end = mid -1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 탐색)
    else:
        result = mid
        start = mid + 1

print(result)