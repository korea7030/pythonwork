# -*- coding: utf-8 -*-
import requests
r = requests.get("http://wikibook.co.kr/wikibook.png")

# 바이너리 형식 저장
with open('test.png', 'wb') as f:
    f.write(r.content)

print('saved')
