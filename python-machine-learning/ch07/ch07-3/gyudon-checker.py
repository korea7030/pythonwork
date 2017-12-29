# -*- coding: utf-8 -*-
import gyudon - keras as gyudon
import sys
import os
from PIL import Image
import numpy as np

# 명령줄에서 파일 이름 지정
if len(sys.argv) <= 1:
    print("gyudon-checker.py <파일이름>")
    quit()

image_size = 50
categories = ["일반 규동", "생강 규동", "양파 규동", "치즈 규동"]
calories = [666, 658, 768, 836]

# 입력 이미지를 numpy로 변환
X = []
files = []

for fname in sys.argv[1:]:
    img = Image.open(fname)
    img = img.convert("RGB")
    img = img.resize((image_size, image_size))

    in_data = np.asarray(img)
    X.append(in_data)
    files.append(fname)

X = np.array(X)

# CNN 모델로 구축
model = gyudon.build_model(X.shape[1:])
model.load_weights("./image/gyudom-model.hdf5")

# 데이터 예측
html = ""
pre = model.predict(X)

for i, p in enumerate(pre):
    y = p.argmax()
    print("입력 : ", files[i])
    print("규동 이름 : ", categories[y])
    print("칼로리 : ", calories[y])

    html += """
    <h3> 입력 : {0} </h3>
    <div>
        <p><img src="{1}" width=300></p>
        <p>규동이름 : {2}</p>
        <p>칼로리 : {3} </p>
    </div>
    """.format(os.path.basename(files[i]), files[i], categories[i], calories[i])


# 리포트 저장하기 --- (※5)
html = "<html><body style='text-align:center;'>" + \
    "<style> p { margin:0; padding:0; } </style>" + \
    html + "</body></html>"
with open("gyudon-result.html", "w") as f:
    f.write(html)
