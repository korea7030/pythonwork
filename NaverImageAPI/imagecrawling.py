# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:28:15 2016

@author: Administrator
"""
import sys
import urllib.parse
import urllib.request
import requests
from lxml import etree

param_len = len(sys.argv)

if param_len == 3:    
    client_id = 'apo0QkBvJ8zCcKtDJZJL' # client id
    client_secret = 'v7cEvaCwsO' # client secret 
    url = 'https://openapi.naver.com/v1/search/image.xml?' # url
    
    data = sys.argv[1]
    folder = sys.argv[2]
    
    params = urllib.parse.urlencode({'query': data, 'display': 100, 'sort' : 'sim'})
    
    # header 설정
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }
    
    # get xml
    res = requests.get(url+params, headers = headers)
    
    xp = etree.fromstring(res.content)
    
    ## link tag 
    links = xp.xpath("//link/text()")
    i = 0
    
    for lst in links[1:len(links)]:
        img = requests.get(lst)
        filename = folder+"//"+data+str(i)+".jpeg"
        
        with open(filename, 'wb') as f:
            f.write(img.content)    
        
        i=i+1
        
        if i==100 :
            i = 0
else:
    print ("parameter 를 입력하세요")