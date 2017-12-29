# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:41:58 2015

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
plt.show()  # 그래프

# density 밀집도 구하기
nx.density(g)

# 한 노드가 가지고 있는 타이개수 : degree
# in-degree : popular 함 / out-degree  : active 함

# 중심의 위치에 있는 거는 central 을 의미
# degree centrallity : 관계의 수를 가지고 나타냄
# Closeness centerality : 다른 관게와 얼마나 가까이 있는지
# Betweenness centrality : 가운데에 얼마나 많이 있느냐
# Eigenvector centrality : 중요한 노드랑 얼마나 연결되어 있는지
