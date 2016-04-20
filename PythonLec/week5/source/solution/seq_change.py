# coding: UTF-8
# 단어의 순서를 바꿔서 출력하라.

s = "Sometimes I feel like a data scientist"

for item in s.split()[::-1]:
	print(item, end=" ")