# coding: utf-8
# 문제: title에서 Hashtag만 가져와 List에 담기

# 게시글 제목
# 한줄이 길어질 때는 역슬래시(\) 이용
title = "On top of the world! Life is so fantastic if you just let it. \
I have never been happier. #nyc #newyork #vacation #traveling"

# Write your code below.
hashtags = []
for item in title.split():
	if item.startswith("#"):
		hashtags.append(item[1:])

print(hashtags)