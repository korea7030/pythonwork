# -*- coding: utf-8 -*-
"""
곱하기 혹은 더하기
 - (0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼족부터 오른쪽으로 하나씩 모든 숫자를 확인하여, 숫자 사이에
   'x' 혹은 '+' 연산자를 넣어 만들어낼 수 있는 가장 큰 수를 구한다

 두 수가 1 이하이면 +, 아니면 x를 해야 함
"""
data = input()

result = int(data[0])


for i in data:
    num = int(i)
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)