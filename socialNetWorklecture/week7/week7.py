# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:52:06 2015

@author: Administrator
"""

import os
import requests
import codecs  # 한글 저장된 파일 핸들링 위한 module
from bs4 import BeautifulSoup  # bs4 모듈 중에 BeautifulSoup만 사용 하고자 할 경우
import selenium

os.chdir('C:\\pythonwork\\week7')

# 하위 chlid tag를 가져올 경우 -> 변수명.contents.text

# 상위 parent tag를 가져올 경우 -> 변수명.parent.text

# 같은 단계의 tag를 가져올 경우
# -> 변수명.next_sibling.contents[index번호].text or 변수명.previous_sibling.contents[index번호].text

# 우리 나라의 주식 주가는
r = requests.get("http://finance.daum.net/quote/index.daum?nil_profile=stockgnb&nil_menu=sise_top")
text = r.text
soup = BeautifulSoup(text)

print(soup)
# list형태로 받아옴. 뒤에 .text 넣으면 작동 안함.
cUp = soup.find_all('dd', class_='point cUp')

# 환율, 유가, 다우존스 정보
cost_num = soup.find_all('span', class_='cost num')

# 위치확인
cost_num[0]
cost_num[1]
cost_num[3]


print(cUp)
# 출력결과
# 첫번째(list 0번째) : [<dd class="point cUp">2,040.40</dd>,
# 두번쟤(list 1번째) :  <dd class="point cUp">681.97</dd>,
# 세번째(list 2번째) :  <dd class="point cUp">249.41</dd>]

KOSPI = cUp[0].text
KOSDAQ = cUp[1].text
KOSPI200 = cUp[2].text

print(str(KOSPI), str(KOSDAQ), str(KOSPI200))

# 파일 저장
fw = codecs.open("daum_result.txt", encoding="utf-8", mode="w")
fw.write(str(KOSPI) + ";" + str(KOSDAQ) + ";" + str(KOSPI200) + ";" +
         str(cost_num[0].text) + ";" + str(cost_num[1].text) + ";" + str(cost_num[3].text))
# cost_num[0]
# cost_num[1]
# cost_num[3]
fw.close()
##


# selenium  기능
# 1. browser 실행 (접근할 URL 지정 필요)
# 2. url 페이지 접근 -> server 요청(source code1)
# 3. 사용자 input 값을 수행 -> server 요청(source code2)
# 4. selenium.get 하면 source code2 정보 다운
