# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:18:59 2015

@author: Administrator
"""

import requests
import codecs
import time
import os
from bs4 import BeautifulSoup

## 시스템 경로 설정
os.getcwd()
os.chdir("C:/pythonwork/HW1_PY")

url_base='http://www.yes24.com/24/goods/'

## 전체 정보를 저장하는 변수
info = '' 

## title split 을 위한 변수
title_split = []

## 결과를 담을 파일
f=codecs.open('U2015046.txt',encoding='utf-8', mode='w')

fr = codecs.open('book_id.txt', 'r', 'utf-8')

## bookid를 가져오기 위한 파일 불러오기
for line in fr.readlines() :

    bookid = line.strip()
    print(bookid)
    
    ## 파일내 가져온 값이 "Book_id"일 경우 continue
    if (bookid == 'Book_id'):
        continue
    
    full_url = url_base + bookid
    
    print(full_url)
    
    time.sleep(1) ## 1초 쉬기.
    
    r=requests.get(full_url)
    
    text=r.text
    
    soup=BeautifulSoup(text)
    ## 해당 id의 경우는 할인율의 tag가 존재하지 않아, yes_b에 해당하는 할인가만 받아서 처리
    if bookid == "20193639" :
        book_title = soup.find('title').text
        title_split = book_title.split(",")
        print("book_title : "+title_split[0])
        book_sales = soup.find('em',class_='yes_b').text
        print("sales : "+book_sales)
        info = bookid+'|'+title_split[0]+'|'+book_sales
        print(info)
    ## 나머지는 제목|판매가|할인율 순으로 처리
    else :    
        book_title = soup.find('title').text
        title_split = book_title.split(",")
        print("book_title : "+title_split[0])
        book_sales = soup.find('em',class_='yes_b').text
        print("sales : "+book_sales)
        book_rate = soup.find('span',class_='price').text
        print("rate : "+book_rate)
        info = bookid+'|'+title_split[0]+'|'+book_sales+'|'+book_rate
        print(info)
    
    ## 파일 쓰기
    f.write(info+"\n")
    
    ## full_url변수 초기화
    full_url = ''

## 읽은 파일 닫기
fr.close()
## 쓴 파일 닫기
f.close()