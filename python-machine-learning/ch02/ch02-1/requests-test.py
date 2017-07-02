# -*- coding: utf-8 -*-
import requests
r = requests.get("http://api.aoikujira.com/time/get.php")

# 텍스트 형식 출력
text = r. text
print(text)

# 바이너리
bin = r.content
print(bin)
