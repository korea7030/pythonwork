# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import os
import re

# 파일 경로 지정
search_dir = "./image/101_ObjectCategories"
cache_dir = "./image/cache_avhash"

if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)

# 이미지 데이터를 Average Hash 로 변환


def average_hash(fname, size=16):
    fname2 = fname[len(search_dir):]
    # 이미지 캐시하기
    cache_file = cache_dir + "/" + fname2.replace("/", "_") + ".csv"
    if not os.path.exists(cache_file):
        img = Image.open(fname)
        img = img.convert('L').resize((size, size), Image.ANTIALIAS)
        pixels = np.array(img.getdata()).reshape((size, size))
        avg = pixels.mean()
        px = 1 * (pixels > avg)
        np.savetxt(cache_file, px, fmt="%.0f", delimiter=",")
    else:  # 캐시돼 있으면 읽지 않음.
        px = np.loadtxt(cache_file, delimiter=",")
    return px

# 해밍 거리 구하기


def hamming_dist(a, b):
    aa = a.reshape(1, -1)  # 1차원 배열로 변환
    ab = b.reshape(1, -1)
    dist = (aa != ab).sum()
    return dist

# 모든 폴더에 처리 적용


def enum_all_files(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            fname = os.path.join(root, f)
            if re.search(r'\.(jpg|jpeg|png)$', fname):
                yield fname

# 이미지 찾기


def find_image(fname, rate):
    src = average_hash(fname)
    for fname in enum_all_files(search_dir):
        dist = average_hash(fname)
        diff_r = hamming_dist(src, dist) / 256

        if diff_r < rate:
            yield (diff_r, fname)


# 찾기
srcfile = search_dir + "/chair/image_0016.jpg"
html = ""
sim = list(find_image(srcfile, 0.25))
sim = sorted(sim, key=lambda x: x[0])

for r, f in sim:
    print(r, ">", f)
    s = '<div style="float:left;"><h3>[ 차이 :' + str(r) + '-' + \
        os.path.basename(f) + ']</h3>' + \
        '<p><a href="' + f + '"><img src="' + f + '" width=400>' + \
        '</a></p></div>'

    html += s

html = """<html><head><meta charset="utf8"></head>
<body><h3>원래 이미지</h3><p>
<img src='{0}' width=400></p>{1}
</body></html>""".format(srcfile, html)
with open("./avhash-search-output.html", "w", encoding="utf-8") as f:
    f.write(html)
print("ok")
