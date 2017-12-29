# -*- coding: utf-8 -*-
# 단어를 ID로 변환하고 출현 횟수 구하기
import os
import glob
import json

root_dir = "./newstext"
dic_file = root_dir + "/word-dic.json"
data_file = root_dir + "/data.json"
data_file_min = root_dir + "/data-mini.json"

# 어구를 자르고 ID로 변환
word_dic = {"_MAX": 0}


def text_to_ids(text):
    text = text.strip()
    words = text.split(" ")
    result = []
    for n in words:
        n = n.strip()
        if n == "":
            continue
        if not n in word_dic:
            wid = word_dic[n] = word_dic["_MAX"]
            word_dic["_MAX"] += 1
            print(wid, n)
        else:
            wid = word_dic[n]
        result.append(wid)
    return result

# 파일을 읽고 고정 길이의 배열 리턴


def file_to_ids(fname):
    with open(fname, "r") as f:
        text = f.read()
        return text_to_ids(text)

# 딕셔너리에 단어 모두 등록


def register_dic():
    files = glob.glob(root_dir + "/*/*.wakati", recursive=True)
    print(files)
    for i in files:
        file_to_ids(i)

# 파일 내부의 단어 세기


def count_file_freq(fname):
    cnt = [0 for n in range(word_dic["_MAX"])]
    with open(fname, "r") as f:
        text = f.read().strip()
        ids = text_to_ids(text)
        for wid in ids:
            cnt[wid] += 1

# 카테고리마다 파일 읽어 들이기


def count_freq(limit=0):
    X = []
    Y = []
    max_words = word_dic["_MAX"]
    print("max_words : ", max_words)

    cat_names = []
    for cat in os.listdir(root_dir):
        cat_dir = root_dir + "/" + cat
        print("cat_dir : ", cat_dir)

        if not os.path.isdir(cat_dir):
            continue
        cat_idx = len(cat_names)
        cat_names.append(cat)
        print("cat_names : ", cat_names)

        files = glob.glob(cat_dir + "/*.wakati")
        i = 0
        for path in files:
            print("path : ", path)
            cnt = count_file_freq(path)
            X.append(cnt)
            Y.append(cat_idx)
            if limit > 0:
                if i > limit:
                    break
                i += 1
    return X, Y


# 단어 딕셔너리 만들기
if os.path.exists(dic_file):
    word_dic = json.load(open(dic_file))
    # print(json.dumps(word_dic))
else:
    register_dic()
    json.dump(word_dic, open(dic_file, "w"))

# 벡터를 파일로 출력
# 테스트 목적의 소규모 데이터 생성
X, Y = count_freq(20)
json.dump({"X": X, "Y": Y}, open(data_file_min, "w"))
# 전체 데이터를 기반으로 데이터 만들기
X, Y = count_freq()
json.dump({"X": X, "Y": Y}, open(data_file, "w"))
print("ok")
