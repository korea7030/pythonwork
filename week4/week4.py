# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 10:39:58 2015

@author: Administrator
"""

import os  ## 현재 pc에 설정된 os에 관련된 설정
os.getcwd()  ## 현재 working directory 가져오기
os.chdir("C:\pythonwork\week4") ## working directory 변경

############ 1~100 까지 제곱 #################

fw = open('multiple_result.txt','w')  ## 제곱결과 나타낼 파일

gop = 0;    ## 제곱 저장할 변수
for k in range(1,101) : ## 1~100까지 k를 100번 돌림
    gop = k*k
    ## write할 때 str() 문자 형태로 변환해서 저장
    ## str붙이는 이유는 파일에 쓸때 문자로만 저장됨. 
    ## 확장자를 바꿔봤지만 여전히 똑같은 에러가 남 
    ## 파일에 쓰기위한 필수과정
    fw.write(str(k)+ ":" +str(gop)+"\n")    
    print(gop)  ## 결과 화면에 뿌려주기
    
fw.close() ## 파일 닫기


###########################################
################scrapping##################
import requests  ## 웹페이지 요청위한 모듈

f = open('amazone_code.txt','w')  ## 파일열기
r = requests.get("http://www.amazon.com/gp/product/1449355730?keywords=python%20in%20books&qid=1443840422&ref_=sr_1_4&s=books&sr=1-4")  ## 해당 url의 html내용 받기
r.text
## repr : 모든 문자를 string으로 변환
f.write(repr(r.text)) ## 파일 저장
f.close()
###########################################
