# -*- coding: utf-8 -*-
from sklearn import svm, metrics
import glob, os.path, re, json

# 텍스트를 읽어 빈도 조사
def check_freq(fname):
    name = os.path.basename(fname)
    lang = re.match(r'^[a-z]{2,}', name).group()
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.lower() # 소문자 변환

    # print("text : ", text, "\r\n")
    cnt = [0 for n in range(0,26)] # 영문자 알파벳 수만큼 counting 변수 초기화
    code_a = ord('a')
    code_z = ord('z')

    # 알파벳 출현횟수 구하기
    for ch in text:
        # print ("ch = ", ch)
        n = ord(ch)
        # print(n)
        if code_a <= n <= code_z: # a-z 사이에 있을 때
            cnt[n - code_a] +=1

    print("cnt : ", cnt, "\r\n")
    # 정규화 하기
    total = sum(cnt)
    freq = list(map(lambda n: n/ total, cnt))
    return (freq, lang)

# 각 파일 처리하기
def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)

    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])

    return {"freqs" : freqs, "labels" : labels}

data = load_files("./lang/train/*.txt")
test = load_files("./lang/test/*.txt")

# 이후를 대비해서 JSON으로 결과 저장
with open("./lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)

#학습하기
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])
pred = clf.predict(test["freqs"])

# 결과 테스트
ac_score = metrics.accuracy_score(test["labels"], pred)
cl_report = metrics.classification_report(test["labels"], pred)
print("정답률 =", ac_score)
print("리포트 = ", cl_report)
