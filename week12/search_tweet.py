﻿#-*- coding: utf-8 -*-
from __future__ import print_function
import twitter
import json
import codecs


OAUTH_TOKEN='260006942-4e6HXmAPsRMG3R8tgzS1DBFrCbCrRLar89gQsJBg'
OAUTH_TOKEN_SECRET='UQZTLcHAIaanRFATLNwcNpmgrJGK5jJIEF5vrCvuDDt9p'
CONSUMER_KEY='5rLmSnmix1DiRX9q8MzAA'
CONSUMER_SECRET='66YSjMIY6ACCGFPk6D7IpcwCmpdFaMOnyvCc0do8PMA'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q='도용금지'
#q="#LHHATL"
count=100
search_results=twitter_api.search.tweets(q=q, count=count)
text1=search_results['statuses'][0]['text']
print(text1)

search_results=json.dumps(search_results, indent=1)

f=codecs.open('search_results0620.txt', encoding='utf-8', mode='w')
#f_us = open('us_search_results0425.txt','w')
f.write(search_results)
#f_us.write(search_results)
f.close()
#f_us.close()