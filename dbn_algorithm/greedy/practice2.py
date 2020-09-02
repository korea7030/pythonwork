# -*- coding: utf-8 -*-
"""
숫자 카드 게임
 - 여러 개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드를 구함
 Rule
   1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. N은 행, M은 열
   2. 뽑고자 하는 행 선택
   3. 숫자가 가장 낮은 카드를 뽑는다
"""
N, M = map(int, input().split())
result = 0

for i in range(N):
    data = list(map(int, input().split()))
    # 열의 개수가 안맞으면 break
    if M != len(data):
        break

    # 선택한 행의 가장 작은 수
    min_value = min(data)
    # 결과값, 선택한 수 중 큰 수 구하기
    result = max(result, min_value)

print(result)
