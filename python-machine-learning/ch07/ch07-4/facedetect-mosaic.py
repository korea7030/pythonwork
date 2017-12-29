# -*- coding: utf-8 -*-
import cv2
import sys
import re

# 입력파일 지정
if len(sys.argv) <= 1:
    print("no input file")
    quit()

image_file = sys.argv[1]

# 출력 파일 이름
output_file = re.sub(r'\,jpg|jpeg|PNG$', '-mosaic.jpg', image_file)
mosaic_rate = 30

# 케스케이드 파일 지정
cascade_file = "C:/opencv/build/etc/haarcascades/haarcascade_frontalface_alt.xml"

# 이미지 파일 읽기
image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 인식 실행
cascade = cv2.CascadeClassifier(cascade_file)
face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

if len(face_list) == 0:
    print("no face")
    quit()

# 확인할 부분 모자이크 걸기
print(face_list)
color = (0, 0, 255)

for (x, y, w, h) in face_list:
    # 얼굴 부분 자르기
    face_img = image[y:y + h, x:x + w]
    # 자른 이미지를 지정한 배율로 확대/축소
    face_image = cv2.resize(face_img, (w // mosaic_rate, h // mosaic_rate))
    # 확대/축소한 그림을 원래 크기로
    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)

    # 원래 이미지에 붙이기
    image[y:y + h, x:x + w] = face_img

# 랜더링 결과 출력
cv2.imwrite(output_file, image)
