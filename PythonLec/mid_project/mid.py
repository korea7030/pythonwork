# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:15:35 2016

@author: Administrator
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt # plot 관련
import matplotlib.font_manager # font 관련
import seaborn as sns
from datetime import datetime

%matplotlib inline

book = pd.read_excel('book.xlsx', encoding = "utf-8")
book.head()
book.describe()

book_times = pd.read_excel('book_times.xlsx')
book_times.describe()

for f in matplotlib.font_manager.fontManager.ttflist:
    print (f.name)

# print ([f.name for f in matplotlib.font_manager.fontManager.ttflist]) # 한글 지원되는 font 명 확인
book['Month'] = book['Started Reading'].dt.month

matplotlib.rc('font', family='HCR Dotum') # font 지정
# 카테고리별 읽은 책
cate_g = sns.factorplot('Category', kind = 'count', data=book,aspect=1.5, palette="muted")
cate_g.fig.suptitle("카테고리별 책 수")
cate_g.set_ylabels("책 수")
cate_g.fig.subplots_adjust(top=.9)

borrow_g = sns.factorplot('Borrowed', kind = 'count', data=book, aspect = 1.5, palette = "muted")
borrow_g.fig.suptitle("빌림 여부 확인")
borrow_g.set_ylabels("책 수")
borrow_g.fig.subplots_adjust(top=.9)

Format_g = sns.factorplot('Format', kind='count', data=book, aspect=1.5, palette="muted")
Format_g.fig.suptitle("수단 별 책 수")
Format_g.set_ylabels("책 수")
Format_g.fig.subplots_adjust(top=.9)

Month_g = sns.factorplot('Month', kind='count', data=book, aspect=1.5, palette = 'muted')
Month_g.fig.suptitle("월별 읽은 책 수")
Month_g.set_ylabels("책 수")
Month_g.fig.subplots_adjust(top=.9)

Week_g = sns.factorplot('Have Weekend', kind = 'count', data=book, aspect=1.5, palette = 'muted')
Week_g.fig.suptitle("주말 넘김 여부에 따른 책 수")
Week_g.set_ylabels("책 수")
Week_g.fig.subplots_adjust(top=.9)

Week_df = book[book['Have Weekend'] == 'Y' ]
No_Week_df = book[book['Have Weekend'] == 'N' ]
Week_df.head()

WeekRat_g = sns.factorplot('Rating', kind='count', data= Week_df)
WeekRat_g.fig.suptitle("별점 별 책 현황(주말)")
WeekRat_g.set_ylabels("책 수")
WeekRat_g.fig.subplots_adjust(top=.9)

NoWeekRat_g = sns.factorplot('Rating', kind='count', data= No_Week_df)
NoWeekRat_g.fig.suptitle("별점 별 책 현황(주중)")
NoWeekRat_g.set_ylabels("책 수")
NoWeekRat_g.fig.subplots_adjust(top=.9)

Week_df['Read Reason'].value_counts()
No_Week_df['Read Reason'].value_counts()
Week_df[Week_df['Read Reason'] != '검색']
## 주말포함하여 확인 했을 때, 대체적으로 내가 고른 책이 많음 .

book_times.head()
book_times['Read Page Num'] = book_times['End Page Num'] - book_times['Start Page Num']
book_times['Spent time'] = ((book_times['End Read Time']- book_times['Start Read Time']).dt.seconds % 3600) // 60

plt.scatter(book_times['Read Page Num'], book_times['Spent time'])
plt.title('페이지수와 읽은 시간')
plt.xlabel('페이지 수')
plt.ylabel('읽은 시간(분)')
plt.xlim(0, book_times['Read Page Num'].max()+20)
plt.ylim(0, book_times['Spent time'].max()+10)
plt.gca().set_aspect('equal', adjustable='box')
