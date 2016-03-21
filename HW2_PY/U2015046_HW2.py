# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:14:16 2015

@author: Administrator
"""
import requests
import json
from bs4 import BeautifulSoup
from scipy.stats.stats import pearsonr
import re

def get_points(player) :
    base_html='http://www.kongregate.com/accounts/'  
    player_url = base_html+player
    print(player_url)
    r = requests.get(player_url)
    
    player_html = r.text    
    is_private = re.compile('profile is private.')
    
    if(not re.findall(is_private, player_html)) : 
        soup = BeautifulSoup(player_html)
        user_data = soup.find(id='user_points').find_next().find_next_sibling().text
        points = user_data
    else :
        points = 0
        
    return points

gamer_point= []  ## gamer point 점수(50명)
gamer_fr_point = []  ## gamer의 친구 point 평균 점수

f=open('U2015046_HW2.txt','w')
game_ids = open('user_ids.txt', 'r')

friend_html_pre = 'http://api.kongregate.com/api/user_info.json?username='
friend_html_end = '&friends=true'

for line in game_ids.readlines() :
     gid = line.strip()
     # print(gid)
     point = get_points(gid)
     gamer_point.append(int(point))         
     # playerid 로 친구정보 가져오기 위한 json url 
     json_url = friend_html_pre + gid + friend_html_end     
     # json url request 
     friend_html = requests.get(json_url)
     # json 변환
     js = json.loads(friend_html.text)         
     # 친구목록 가져오기
     friend_list = js['friends']
     
     friend_point_sum = 0 # 친구 point 정보 누적합계 변수
     friend_point_avg = 0 # 친구 point 정보 평균 변수
     
     if (len(friend_list) != 0) :  ## 친구 list가 있는경우
         for name in friend_list:
             print(name)
             # 친구 point 정보 검색 시작
             fr_point = get_points(name)
             friend_point_sum += int(fr_point) 
             
         friend_point_avg = friend_point_sum / len(friend_list)
         print(gid+"의 친구 point 누적 합 : "+str(friend_point_sum))
         print(gid+"의 친구수 : "+str(len(friend_list)))
         
         f.write(gid+"의 친구 point 누적 합 : " + str(friend_point_sum)+" / ")
         f.write(gid+"의 친구 수 : " + str(len(friend_list))+" = ")    
         f.write(str(friend_point_avg)+"\n")
         # 친구들의 평균을 계산한 점수를 list에 추가
         gamer_fr_point.append(friend_point_avg)
     else : # 친구 list가 없는 경우
       f.write(gid + "의 친구 정보 없음\n")
       friend_point_avg = 0  # 평균 0
       gamer_fr_point.append(friend_point_avg)
       continue

game_ids.close()
# 상관게수
f.write("\n"+"gamer point 리스트 : "+str(gamer_point)+'\n')
f.write("각 gamer 친구 평균 point 리스트 : "+str(gamer_fr_point)+'\n\n')
f.write("gamer/gamer fiend 간의 상관계수 : "+str(pearsonr(gamer_point, gamer_fr_point)))

f.close()
