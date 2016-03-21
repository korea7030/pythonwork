# -*- coding: utf-8 -*-

import requests
import bs4 
import time 
import codecs

def getTopRank() :
    naver_url = 'http://www.naver.com'
    
    #1) 요청
    response = requests.get(naver_url)
    
    #2) 응답으로 HTML추출
    html_content = response.text.encode(response.encoding)
    
    
    #3) HTML 파싱
    navigator = bs4.BeautifulSoup(html_content)
    
    #4) 네비게이터를 이용해 원하는 태그 리스트 가져오기
    realRankTag = navigator.find_all(id='realrank')
    resultList = realRankTag[0].find_all('a')
    
    #5) 키워드 추출
    keywords = [item['title'] for item in resultList]
    
    print '=============='
    print time.ctime()
    time_clock = time.strftime("%Y%m%d%H%M%S", 
              time.gmtime(time.mktime(time.strptime(time.ctime(), 
                                                 "%a %b %d %H:%M:%S %Y"))))
    ##print()
    print ''
    f = codecs.open(str(time_clock)+'.txt',encoding='utf-8', mode='w')    
    #6) 키워드 출력
    for index, keyword in enumerate(keywords):
        if index == 10:
            break;
        
        resultText = '[%d위] %s'%(index+1, keyword.encode('utf-8'))
        f.write(resultText.decode('utf-8')+"\n")
        print resultText.decode('utf-8').encode('euc-kr')
        
        
    f.close();
    print ''
    
daemon_flag= True
    
def Daemon():
    while(daemon_flag):
        getTopRank();
        time.sleep(5)
    
if __name__ == '__main__': 
    Daemon() 

            
Daemon()