from __future__ import print_function

import requests
import codecs

#f = open("daum_source.txt","w")
f = codecs.open('daum_source.txt', encoding='utf-16', mode='w')
r = requests.get('http://www.daum.net')
# print(r.text)

f.write(r.text)
f.close()
