# coding: UTF-8
# 주어진 문장을 모두 소문자로 만들고 ',', '.'을 제거하라.
# 그리고 각 단어가 몇 개 사용했는지 Counting하라.

s = 'We propose to start by making it possible to teach programming in Python, \
an existing scripting language, and to focus on creating \
a new development environment and teaching materials for it.'

s = s.lower().replace(',', '')
s = s.replace('.', '')

for item in s.split():
	print('%s: %d' % (item, s.count(item)))