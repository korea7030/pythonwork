# coding: UTF-8
# 카드 52장 조합 만들기

cards = []
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

for f in front:
	for b in back:
		cards.append(f + b)

print(cards)
print('%d 장' % len(cards))