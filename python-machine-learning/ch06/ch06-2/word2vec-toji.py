# -*- coding: utf-8 -*-
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec

# utf-16으로 인코딩 후 출력
fp = codecs.open("C:\\pythonwork\\python-machine-learning\\ch06\\ch06-1\\2BEXXX09.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.find('body')
text = body.getText()

# 텍스트 한줄 처리
twitter = Twitter()
results = []
lines = text.split("\r\n")
for line in lines:
    # 형태소 분석
    malist = twitter.pos(line, norm=True, stem=True)
    r = []

    for word in malist:
        # 어미 / 조사 등은 제외
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            r.append(word[0])

    rl = (" ".join(r)).strip()
    results.append(rl)
    print(rl)

# 파일로 출력
wakati_file = 'toji.wakati'
with open(wakati_file, "w", encoding="utf-8") as fp:
    fp.write("\n".join(results))

# word2vec 모델 만들기
data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save("kokoro.model")
print("ok")
