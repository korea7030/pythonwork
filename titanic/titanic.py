# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 15:21:42 2015

@author: Administrator
"""

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


def male_female_child(passenger) :
    age, sex= passenger
    if age < 16:
        return 'child'
    else :
        return sex


titanic_df = pd.read_csv('train.csv')
titanic_df.head()
## dataframe의 기본정보
titanic_df.info()

## 1) 타이타닉 호의 승객은??
sns.factorplot('Sex', kind='count', data=titanic_df)

## 2) 남녀의 등급별 승객 수 
sns.factorplot('Pclass', kind='count', hue='Sex', order=[1,2,3], data=titanic_df)

## 남,녀,어린이 구분을 위한 컬럼
titanic_df['person'] = titanic_df[['Age', 'Sex']].apply(male_female_child, axis=1)

## 2-1) 남,녀,어린이의 등급별 승객 후
sns.factorplot('Pclass', kind='count', hue='person', order=[1,2,3], data=titanic_df)

## 나이별 승객 분포 
titanic_df['Age'].hist(bins=70)

## 남,녀,어린이 승객의 수
titanic_df['person'].value_counts()

#==============================================================================
# male      537
# female    271
# child      83
# dtype: int64
#==============================================================================

## deck 정보 가져오기(cabin 컬럼에 정보가 있음 )
deck = titanic_df['Cabin'].dropna()
deck.head()

## deck정보를 담기위한 앞자리 정보만 저장
levels=[]
for level in deck:
    levels.append(level[0])


cabin_df = DataFrame(levels)
cabin_df.columns = ['Cabin']
cabin_df.head()

## 어떤 deck에 승객이 몇명이 있는가#######
sns.factorplot('Cabin', kind='count', data=cabin_df, palette='winter_d')

## 그래프에 T라는 deck이 있는데 이는 없는 deck이므로 
cabin_df = cabin_df[cabin_df.Cabin != 'T']
sns.factorplot('Cabin', kind='count', data=cabin_df, palette='summer')

##########################################

#### 어떤 요소가 승객들을 생존하게 만들었나??? ####
titanic_df["Survivor"] = titanic_df.Survived.map({0 : "no", 1: "yes"})
titanic_df.head()

## 생존자수 확인
sns.factorplot('Survivor', kind='count', data=titanic_df, palette='Set1')

titanic_df['Survivor'].value_counts()

## 등급별 생존확률 확인
sns.factorplot('Pclass', 'Survived', data=titanic_df, order=[1,2,3])

## 남,녀, 어린이 구분 별 생존률 확인
sns.factorplot('Pclass', 'Survived', hue='person', data=titanic_df, order=[1,2,3])

## 나이의 생존율이ㅡ 상관관계 확인
sns.lmplot('Age', 'Survived', data=titanic_df)

## 나이와 생존율에 따른 승객등급 분포 확인
sns.lmplot('Age', 'Survived', hue='Pclass', data=titanic_df)

## 나이와 생존율에 따른 성별 분포 
sns.lmplot('Age', 'Survived', hue='Sex', data=titanic_df)
