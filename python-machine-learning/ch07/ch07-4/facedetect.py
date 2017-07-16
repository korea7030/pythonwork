# -*- coding: utf-8 -*-
import cv2
import sys

# 입력 파일 지정
image_file = "./photo/face1.jpg"

# 케스케이드 파일의 경로 지정
cascade_file = "C:/opencv/build/etc/haarcascades/haarcascade_frontalface_alt.xml"

# 이미지 읽어 들이기
image = cv2.imread(image_file)
# 그레이스케일로 변환하기
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 인식 특징 파일 읽어들이기
cascade = cv2.CascadeClassifier(cascade_file)

# 얼굴인식 실행
face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors =1, minSize=(150,150))

if len(face_list)>0:
    # 인식한 부분 표시
    print(face_list)
    color = (0, 0, 255)
    for face in face_list:
        x,y,w,h = face
        cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness=8)

    # 파일로 출력
    cv2.imwrite("facedetect-output.PNG", image)

else:
    print("no face")
