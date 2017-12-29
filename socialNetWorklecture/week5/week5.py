# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 10:45:30 2015

@author: Administrator
"""

import os  # 현재 pc에 설정된 os에 관련된 설정
import requests
import codecs  # 한글 저장된 파일 핸들링 위한 module

from bs4 import BeautifulSoup  # bs4 모듈 중에 BeautifulSoup만 사용 하고자 할 경우

os.getcwd()  # 현재 working directory 가져오기
os.chdir("C:\pythonwork\week5")  # working directory 변경

# 한글 포함된 파일 읽을 때
f = codecs.open('html_test.txt', encoding='euc-kr', mode='r')
text = f.read()
print(text)

soup = BeautifulSoup(text)
print(soup.title)
print(soup.title.text)
print(soup.span.text)

print(soup.find('span').text)

print(soup.find_all('span'))

# yes24 책 정보 가져오기
r = requests.get('http://www.yes24.com/24/UsedShop/Goods/8805784')
text = r.text

soup = BeautifulSoup(text)

booktitle = soup.find('title')
print(booktitle)

# 판매가와 할인가 저장위한 파일생성
f = codecs.open('result.txt', encoding='utf-8', mode='w')
# 판매가 정보
sales = soup.find('em', class_='yes_b').text
print(sales)
# 할인율 정보
rate = soup.find('span', class_='txt_price').text
print(rate[7:14])
# 저장
f.write(sales + ";" + rate[7:14])
# 파일 닫기
f.close()
rate_str = rate.strip()
rate_str
print(rate.strip())
