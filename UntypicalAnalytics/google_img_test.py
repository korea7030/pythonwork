# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:06:02 2016

@author: Administrator
"""
import requests
import lxml.html
from urllib.parse import urljoin ## 상대주소 처리를 위한 모듈
from bs4 import BeautifulSoup

import urllib, re, random
from os.path import isfile
#from time import sleep
#sleep(15)

# //*[@id="imageResult"]/li[1]/a[1]/img
# #search=%EB%90%9C%EC%9E%A5%EC%B0%8C%EA%B0%9C&page=1
# img_path = './/*[@id="imageResult"]/li[1]/a[1]/img'

url = 'http://letscc.net/?t=all&k=%EB%90%9C%EC%9E%A5%EC%B0%8C%EA%B0%9C'
# search = {'k': '된장찌개'}
r = requests.get(url)
# print (r.encoding)
soup = BeautifulSoup(r.text.encode('cp949'), "lxml")
print (soup.text)

f = open('test.txt', 'w', encoding = "utf8")
f.write(r.text)
f.close()
# root = lxml.html.fromstring(r.text)

# print (root.xpath(img_path))

# root = lxml.html.fromstring(res.text)