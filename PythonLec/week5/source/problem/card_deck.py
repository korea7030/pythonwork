# coding: UTF-8
# 카드 52장 조합 만들기

front = ['s', 'c', 'd', 'h', ]  # Spade, Club, Diamond, Heart
back = [
	'2',
	'3',
	'4',
	'5',
	'6',
	'7',
	'8',
	'9',
	'T',  # Ten
	'J',  # Jack
	'Q',  # Queen
	'K',  # King
	'A',  # Ace
]

res = []
# Write your code below.
for i in front:
  for j in back:
    res.append(i+j)

cnt = len(res)
print(res)
print("count : "+str(cnt))