# -*- coding: utf-8 -*-
"""
문자열 뒤집기
 - 0과 1로 이루어진 문자열 S의 모든 숫자를 같게 만들어야 한다.
   S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것
   S = 0001100 일때
   1. 전체를 뒤집으면 11100111
   2. 4,5번재 문자를 뒤집으면 11111111
   하지만 처음부터 4,5번째 문자를 뒤집으면 00000000이 되어서 1번 만에 같은 숫자로 만들 수 있음

   * 다른숫자가 나올 위치때 count를 세주면 된다
"""
data = input()
count0 = 0
count1 = 0

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))