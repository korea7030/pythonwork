# coding: utf-8
# 문제: title에서 Hashtag만 가져와 List에 담기

# 게시글 제목
# 한줄이 길어질 때는 역슬래시(\) 이용
title = "On top of the world! Life is so fantastic if you just let it. \
I have never been happier. #nyc #newyork #vacation #traveling"

# Write your code below.
a = title.split()
obj = []
for string in a:
   if string.startswith("#"):
        obj.append(string[1:])
print(obj) 