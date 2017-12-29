# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 21:48:33 2016

@author: Administrator
"""

from bs4 import BeautifulSoup
import requests
import re
import urllib
import os


def get_soup(url, header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url, headers=header)))


image_type = "Action"
# you can change the query for the image  here
query = "Terminator 3 Movie"
query = query.split()
query = '+'.join(query)

print(query)

url = "https://www.google.co.in/searches_sm=122&source=lnms&tbm=isch&sa=X&ei=4r_cVID3NYayoQTb4ICQBA&ved=0CAgQ_AUoAQ&biw=1242&bih=619&q=" + query

print(url)
header = {'User-Agent': 'Mozilla/5.0'}
soup = get_soup(url, header)

images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
# print images
for img in images:
    raw_img = urllib.request.urlopen(img).read()
    # add the directory for your image here
    DIR = "C:\\pythonwork\\NaverImageAPI\\negative\\"
    cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
    print(cntr)
    f = open(DIR + image_type + "_" + str(cntr) + ".jpg", 'wb')
    f.write(raw_img)
    f.close()
