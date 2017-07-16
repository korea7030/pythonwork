# -*- coding: utf-8 -*-
from PIL import Image
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split

# 분류 대상 카테고리 선택
caltech_dir = "../image/101_ObjectCategories"
categories = ["chair", "Camera", "butterfly", "elephant", "flamingo"]
nb_classes = len(categories)

# 이미지 크기 지정
image_w = 64
image_h = 64
pixels = image_w * image_h

# 이미지 데이터 읽어 들이기
X = []
Y = []

for idx, cat in enumerate(categories):
    # 레이블 지정
    label = [0 for i in range(nb_classes)]
    label[idx] = 1
    '''
    카테고리 이름 | 레이블 데이터
    chair(0)            [1,0,0,0,0]
    camera(1)        [0,1,0,0,0]
    butterfly(2)      [0,0,1,0,0]
    elephant(3)      [0,0,0,1,0]
    flamingo(4)      [0,0,0,0,1]
    '''
    # 이미지
    image_dir = caltech_dir+"/"+cat
    files = glob.glob(image_dir+'/*.jpg')

    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB") # RGB
        img = img.resize((image_w, image_h)) # 이미지 크기 지정(64 x 64)

        data = np.asarray(img) # numpy 배열로 전환

        X.append(data)
        Y.append(label)

        if i % 10 == 0:
            print(i, "\n", data)

X = np.array(X)
Y = np.array(Y)

# 학습 전용 데이터와 테스트 전용 데이터 구분
X_train, X_test, y_train, y_test = train_test_split(X,Y)

xy = (X_train, X_test, y_train, y_test)
np.save("../image/5obj.npy", xy)

print("ok", len(Y))
