# -*- coding: utf-8 -*-
"""
Created on Wed May 18 22:02:58 2016

@author: Administrator
"""

import requests  # url 요청에 대한 사이트 내용 가져올 모듈 
from konlpy.tag import Kkma # 형태소 분석을 위한 모듈
import lxml.html # url 요청에 대한 html 형식 처리
import csv 
from konlpy.tag import Twitter
from sklearn.feature_extraction.text import CountVectorizer
def extract(url, path):
    res = requests.get(url)
    res.encoding = 'cp949'
    root = lxml.html.fromstring(res.text)
    # print(root.xpath(path).text_content())
    return root.xpath(path)

def get_word(doc):
    nouns = tagger.nouns(doc)
    return [noun for noun in nouns if len(noun) > 1]

    
url = "http://search.chosun.com/search/news.search?query=%EC%83%88%EB%88%84%EB%A6%AC%EB%8B%B9&"
page = "pageno="
url_tail = "&orderby=news&naviarraystr=%EC%B6%9C%EC%B2%98%26%26%5E%26%26categorynamenavigator%26%26%5E%26%26categoryname%26%26%5E%26%26%EC%A1%B0%EC%84%A0%EC%9D%BC%EB%B3%B4%26%26%5E%26%26%EC%A1%B0%EC%84%A0%EC%9D%BC%EB%B3%B4%5E%5E%26%5E%5E%EC%84%B9%EC%85%98%26%26%5E%26%26categoryd2navigator%26%26%5E%26%26categoryd2%26%26%5E%26%26%EC%A0%95%EC%B9%98%26%26%5E%26%26%EC%A0%95%EC%B9%98&kind=&cont1=&cont2=&cont5=&categoryname=&categoryd2=&c_scope=navi&sdate=2016.04.13&edate=2016.05.12&premium="
article_xpath = './/section[@class="result news"]/dl/dt/a'
err_url = []

### 뉴스 저장
with open('chosun.csv', 'w') as f:
    writer = csv.writer(f)
    for page in range(1,2):
        page_url = url+"pageno={}".format(page)+url_tail
        for node in extract(page_url, article_xpath):
            try:                
                title = node.text_content().encode('utf8')
                content_url = node.attrib['href']
                print (title.decode('utf8')+" : "+content_url)
                post_content = extract(content_url, './/div[@class="par"]')[0]
                print (post_content.text_content())                
                writer.writerow([post_content.text_content()])
            except:
                err_url.append(page_url)
                continue

### 뉴스 읽기
news = []
with open('chosun.csv', 'r', newline='\r\n') as f:
    reader = csv.reader(f)
    for row in reader:
        news.append(row[0])

### 형태소 분석기
tagger = Twitter()

### Term-Document matrix 생성
cv = CountVectorizer(tokenizer=tagger.nouns, max_features=50) 
tdf = cv.fit_transform(news)
print (tdf.todense())

### 단어목록 출력
words = cv.get_feature_names()
print (words)

### 한단어 빼기 
cv = CountVectorizer(tokenizer=get_word, max_features=50)
tdf = cv.fit_transform(news)
words = cv.get_feature_names()
words
