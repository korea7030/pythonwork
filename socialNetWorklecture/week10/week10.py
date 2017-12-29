# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:42:45 2015

@author: Administrator
"""

import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()  # 빈 껍데기 그래프 생성

g.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
# node 추가(그래프상의 동그라미)

g.add_edges_from([(1, 3), (2, 4), (2, 5), (2, 6), (3, 4), (4, 6), (5, 6)])
# edge 추가(그래프 상의 관계를 나타내는 선)
nx.draw_networkx(g)  # draw
plt.show()  # 그래프 그리기

# networkx 순서
# 1. g => empty
# 2. node 추가
# 3. edge 추가
# 4 node 속성 추가(attribute)
# 5. edge 속성 추가
g
g.nodes()
g.edges()
# attribute 설정
g.node[1]['age'] = 30
g.node[2]['age'] = 35
g.node[3]['age'] = 40
g.node[4]['age'] = 20
g.node[5]['age'] = 30
g.node[6]['age'] = 50
g.node[7]['age'] = 30

# 음주 선호 횟수 지정
g.node[1]['drinking'] = 1
g.node[2]['drinking'] = 3
g.node[3]['drinking'] = 2
g.node[4]['drinking'] = 4
g.node[5]['drinking'] = 3
g.node[6]['drinking'] = 5
g.node[7]['drinking'] = 3

# 속성 값을 알고자 할 떄
g.node[1]['age']

# attribute 확인
g.neighbors(1)

# node 삭제
g.remove_node('age')

g.neighbors(2)

# peer influence
# 1. informational influence
#   정보적 영향을 받는 경우(내가 사고자하는 물건의 정보가 없는 경우)
# 2. normative influence
#   규범적인 영향(내가 사는 제품에 대해 친구들의 신경을 쓰는 경우)

# 제품구매단계
# 1. awareness 단게
#   해당 제품이나 브랜드에서 인지 해야 하는 경우
#    ex)광고(영화, tv) , 주변인
# 2. decision 단계
#   해당 제품을 구매결정 하는 단계
#    ex) 친구, 경제적 여건, 제품평


############################## 과제2 ##################################
# Research Question : 20명의 player의 point와 그 20명의 친구들의 평균 point의 상관관계

# 1. yyup 친구 list를 가져온다.(api 사용)
# 2. request.get 으로 api로 호출한 친구정보 받기
# json 형태로 받아서 친구 리스트를 뽑아 친구 수를 구해야함.
# 3. 뽑은 친구 이름 사용해서 http://www.kongregate.com/accounts/친구아이디
# 4. 친구 페이지를 들어가서 point 정보를 get(class=user_metric_stat)
# 5. 상관관계 구함

####################################################################
