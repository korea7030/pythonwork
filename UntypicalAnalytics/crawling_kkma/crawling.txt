# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 19:05:32 2016

@author: Administrator
"""

import requests  # url 요청에 대한 사이트 내용 가져올 모듈 
from konlpy.tag import Kkma # 형태소 분석을 위한 모듈
import lxml.html # url 요청에 대한 html 형식 처리

## tag의 xpath 값 생성하는 함수
def extract(url, path):
    res = requests.get(url)
    res.encoding = 'cp949'
    root = lxml.html.fromstring(res.text)
    # print(root.xpath(path).text_content())
    return root.xpath(path)

## 일반명사, 고유명사, 의존명사, 대명사 만을 뽑기 위한 tuple 생성
noun_tag =('NNG','NNP','NNB', 'NP')
## url 
url = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=sec&oid=030&aid=0002470940&sid1=001&lfrom=facebook'
## path
path = './/*[@id="articleBodyContents"]/text()'

## request get 
req = requests.get(url) # url 내용 get

## req에 대한 root 생성
root = lxml.html.fromstring(req.text)
## xpath 생성
xpath = extract(url, path)

## xpath에서 받은 내용 저장을 위한 string 변수
text = "" 
## xpath의 값에서 string만 뽑아 text변수에 저장
for lst in xpath[1:len(xpath)-3]:
    text += lst.replace("\r\n\t\r\n\t","")

## 형태소 분석 위한 변수
Kkma = Kkma()
## 단어와 tag를 담기 위한 dictionary
nouns = []

## tag가 N으로 시작하면서 noun_tag tuple에 포함된 tag의 단어만 뽑기
for word, tag in Kkma.pos(text):
    if tag.startswith('N') and tag in noun_tag:
        nouns.append(word)
        
print (nouns)
