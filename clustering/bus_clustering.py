# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:49:31 2015

@author: Administrator
"""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt 
from string import Template
from sklearn.preprocessing import StandardScaler 
from collections import namedtuple
from sklearn.cluster import DBSCAN


colors = ["FF0000", "00FF00", "0000FF", "FFFF00", "FF00FF", "00FFFF", "000000",
        "800000", "008000", "000080", "808000", "800080", "008080", "808080",
        "C00000", "00C000", "0000C0", "C0C000", "C000C0", "00C0C0", "C0C0C0",
        "400000", "004000", "000040", "404000", "400040", "004040", "404040",
        "200000", "002000", "000020", "202000", "200020", "002020", "202020",
        "600000", "006000", "000060", "606000", "600060", "006060", "606060",
        "A00000", "00A000", "0000A0", "A0A000", "A000A0", "00A0A0", "A0A0A0",
        "E00000", "00E000", "0000E0", "E0E000", "E000E0", "00E0E0", "E0E0E0"]

def generate_busstop(df):
    coos = ',\n'.join(['new google.maps.LatLng(%s, %s)' %(r['y'] ,r['x']) for i, r in df.iterrows()])
    return 'var busstops = [{0}];'.format(coos)

def generate_polyline(valname, df, idx=0):
    coos = ',\n'.join(['new google.maps.LatLng(%s, %s)' %(r['y'] ,r['x']) for i, r in df.iterrows()])
    valcoos =  'var {0} = [{1}];'.format(valname, coos)

    polyline_template = """
                        {0}
                        var {1}_ = new google.maps.Polyline({{
                        path: {1},
                        strokeColor: "#{2}",
                        strokeOpacity: 0.8,
                        strokeWeight: 3
                        }});
                        {1}_.setMap(map);"""

    return polyline_template.format(valcoos, valname, colors[idx])

# data = {'busstops': busstops, 'busroutes':busroutes}
def generate_template_html(data, outfilename='busmap.html'):
    infile = open('map_temp.html')
    template = Template(infile.read())
    map_html = template.substitute(data)
    outfile = open(outfilename, 'w')
    outfile.write(map_html)
                    
if __name__ == '__main__':
         
    bus_df = pd.read_csv('bus.tsv', sep='\t')
    mbus_df = bus_df[bus_df['stationid'] != '0']
    mbus_df = mbus_df[mbus_df['stationid'] != '미정차']
    
    #mbus_df.shape
    # sampling_mbus = mbus_df.loc[np.random.permutation(mbus_df.index)[:200]]
    
    # 정거장 구하기
    #busstops = generate_busstop(sampling_mbus)
    
    # 공통으로 정류하는 횟수 지정
    N_BUSSTOPS = 8
    
    stops = mbus_df['stationid'].value_counts()
    d = stops[stops> N_BUSSTOPS].index.values.tolist()
    mbus_df = mbus_df[mbus_df['stationid'].isin(d)]
    busstop_df = mbus_df.drop_duplicates(subset='stationid', take_last=True)
    
    busstops = generate_busstop(busstop_df)
    busroutes = ''
    i = 0
    for idx, row in busstop_df.iterrows():
        route = bus_df[bus_df['busno']==row['busno']]
        busroutes += generate_polyline('poly'+str(i), route,i)
        i+=1
    
    data = {'busstops': busstops, 'busroutes' : busroutes}
    generate_template_html(data)
    
    
    X = busstop_df[['x', 'y']]
    y = busstop_df['busno']
    # k 값을 10으로 넣고 8번 이상 정류하는 정류장의 중심점 구하기
    km = KMeans(init='k-means++', n_clusters=10, n_init = 10)
    km.fit(X)
    print(km.cluster_centers_)
    
    #kMeans 성능 평가
    cluster_range = range(2,15)
    vmeasures = []
    
    for n_cluster in cluster_range:
        km = KMeans(init='k-means++', n_clusters=n_cluster, n_init = 10)
        km.fit(X)
        
        # print('----------------------------\n')
        # print(n_cluster)        
        vmeasures.append(metrics.silhouette_score(X, km.labels_, metric='euclidean'))
        
    
    plt.plot(cluster_range, vmeasures)
    plt.xlabel('# cluster')
    plt.ylabel('v measure')
    plt.autoscale(tight=True)
    plt.grid()
    plt.show()
    
    #클러스터링 후 시각화 
    best_clusters = 10
    km = KMeans(init='k-means++', n_clusters=best_clusters, n_init=10)
    km.fit(X)
    
    # km_cluster_centers 위치 출력(가장 많이 정류하는 정류장)
    centers= pd.DataFrame(km.cluster_centers_, columns=['x','y'])
    
    busstops = generate_busstop(centers)
    busroutes = ''
    
    data = {'busstops':busstops, 'busroutes':busroutes}
    generate_template_html(data, 'busstop_cluster_centers.html')
    # print(X)
    # DBSCAN에 다양한 매개변수 적용하여 이상치 찾기
    
    X['sx'] = X.x
    X['sy'] = X.y
    
    ss = StandardScaler()
    X['sx'] = ss.fit_transform(X.sx)
    X['sy'] = ss.fit_transform(X.sy)
    # print(X)
    
    Param = namedtuple('Param', ['eps', 'min_samples'])
    params = [Param(0.45, 2), Param(0.30, 2), Param(0.35, 2), Param(0.40, 2), 
                Param(0.45, 4), Param(0.30, 4), Param(0.35, 4), Param(0.40, 4), 
                Param(0.45, 3), Param(0.30, 3), Param(0.35, 3), Param(0.40, 3)]
    # print(X.values)
    for param in params:
        dbscan = DBSCAN(eps=param.eps, min_samples=param.min_samples).fit(X[['sx', 'sy']].values)
        labels = dbscan.labels_
        outliers = X[labels == -1]
        
        print(param)
    #     print(labels)
        print(outliers)
    #     print("V-measure: %0.3f" % metrics.v_measure_score(y, labels))
        print(metrics.silhouette_score(X, labels, metric='euclidean'))
    
    # busstops = generate_busstops(outliers)
    # busroutes = ''
        
    # data = {'busstops': busstops, 'busroutes': busroutes}
    # generate_template_html(data, 'busstop_cluster_outlier.html')
    
    #2 시각화
    best_param = Param(eps=0.3, min_samples=2)
    dbscan = DBSCAN(eps=best_param.eps, min_samples=best_param.min_samples).fit(X[['sx', 'sy']].values)
    labels = dbscan.labels_
    outliers = X[labels == -1]
    
    busstops = generate_busstop(outliers)
    busroutes = ''
        
    data = {'busstops': busstops, 'busroutes': busroutes}
    generate_template_html(data, 'busstop_cluster_outlier.html')