from __future__ import print_function
import requests
import codecs

from bs4 import BeautifulSoup

r=requests.get('http://www.yes24.com/24/goods/16667748')

soup=BeautifulSoup(r.text)
book_title=soup.title.text
print(soup.find('em', class_='yes_b').string)
print(book_title)
#f=codecs.open('yes24.txt',encoding='utf-16',mode='w')
#f=open('yes24_no_codec.txt','w') This will generate an error
#f.write(r.text)
#f.write(book_title)
#f.close()

