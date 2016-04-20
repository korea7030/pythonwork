# coding: UTF-8
# 단어의 순서를 바꾸고
# 단어의 글자 순서도 바꿔 출력하라.
# tsitneics atada a ekil leef I semitemoS"

s = "Sometimes I feel like a data scientist"

for item in s.split()[::-1]:
	for char in item[::-1]:
		print(char, end="")
	print(end=" ")