# -*- coding: utf-8 -*-
"""
성적 낮은 순서로 출력(p. 180)
"""
n = int(input())

data = []
for i in range(n):
    input_data = input().split()
    # 글자 숫자 입력 후 저장 시
    data.append((input_data[0], int(input_data[1])))  # 이름, 점수

# key를 이용하여 점수를 기준으로 오름차순
sort_data = sorted(data, key=lambda student: student[1])

for student in sort_data:
    print(student[0], end=' ')