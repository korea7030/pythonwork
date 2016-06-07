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
import numpy as np
import operator
from wordcloud import WordCloud
from matplotlib import pyplot
# %matplotlib inline
import networkx

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

## 단어별 출현빈도
count_mat = tdf.sum(axis=0) # 열별로 단어별 출현 빈도 합계 구함(axis = 1 , 각 문서별 명사의 사용 개수)
count_mat

count = numpy.squeeze(numpy.asarray(count_mat)) # 대괄호가 하나로 줄어듬. 좀더 데이터 핸들링을 쉽게 하기 위해 리스트 형태로 해줌
count

word_count = list(zip(words, count)) # zip : 두개의 각 리스트별 원소의 짝을 지어줌

## 빈도수 정렬
sorted(word_count, key=operator.itemgetter(1), reverse=True) # word_count를 1번째(빈도수)를 기준으로 내림차순 정렬을 하라

## 워드 클라우드 
wc = WordCloud(font_path='C:\\Windows\\Fonts\\malgun.ttf', background_color='white', width=400, height=300)
cloud = wc.generate_from_frequencies(word_count)

pyplot.figure(figsize=(12, 9))
pyplot.imshow(cloud)
pyplot.axis("off")
pyplot.show()


## 단어간 상관계수
word_corr = numpy.corrcoef(tdf.todense(), rowvar=0) # 상관계수 구하기(rowvar =0 : 컬럼단위 상관계수, 1이면 문서간의 상관계수)
word_corr

## 상관계수 높은 단어 100개 
edges = []
for i in range(len(words)): 
    for j in range(i + 1, len(words)): 
        edges.append((words[i], words[j], word_corr[i, j])) # 1이 아닌 및부분의 상관계수 추리기

edges = sorted(edges, key=operator.itemgetter(2), reverse=True) # 상관게수가 높은걸로 정렬
edges = edges[:50]
edges

edge_list = [(word1, word2) for word1, word2, weight in edges]
weight_list = [weight for word1, word2, weight in edges]

## 상관관게 시각화
G = networkx.Graph() # 그래프 생성

edge_set = set()
for word1, word2, weight in edges:
    G.add_edge(word1, word2, weight=weight) # 노드간의 연결선을 추가(단어간의 관계)
    edge_set.add((word1, word2))
    
# spring_layout : edge를 스프링처럼 사용하여 단어간의 자성이 있는 것처럼 밀어내거나 당기는 물리학 시뮬레이션으로 위치를 나타냄
# 서로 연결이 잘 되있을수록 가깝게 연결되어 나옴
# 항상 랜덤이다
# iterations 가 커질수록 안정적으로 나온다.
position = networkx.spring_layout(G, iterations=30) 
pyplot.figure(figsize=(12, 9)) # 그래프 크기
networkx.draw_networkx_nodes(G, position, node_size=0) # 노드추가
networkx.draw_networkx_edges(G, position, edgelist=edge_list, width=weight_list, edge_color='lightgray') # edge 추가
networkx.draw_networkx_labels(G, position, font_size=15, font_family='Malgun Gothic') # 노드의 단어
pyplot.axis('off')
pyplot.show()