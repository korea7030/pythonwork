#-*- coding: utf-8 -*-
from __future__ import print_function

import twitter
import json
import codecs
#import sys
# sys.setdefaultencoding("utf-8")
#import site

OAUTH_TOKEN = '260006942-4e6HXmAPsRMG3R8tgzS1DBFrCbCrRLar89gQsJBg'
OAUTH_TOKEN_SECRET = 'UQZTLcHAIaanRFATLNwcNpmgrJGK5jJIEF5vrCvuDDt9p'
CONSUMER_KEY = '5rLmSnmix1DiRX9q8MzAA'
CONSUMER_SECRET = '66YSjMIY6ACCGFPk6D7IpcwCmpdFaMOnyvCc0do8PMA'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

# print twitter_api

# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424977
SKOREA_WOE_ID = 23424868
SEOUL_WOE_ID = 1132599


# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

#world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
#us_trends = twitter_api.trends.place(_id=US_WOE_ID)
#korea_trends = twitter_api.trends.place(_id=SKOREA_WOE_ID)
seoul_trends = twitter_api.trends.place(_id=SEOUL_WOE_ID)
name1 = seoul_trends[0]['trends'][0]['name']

print(name1)

#seoul_trends=json.dumps(seoul_trends, indent=1)

#us_trends=json.dumps(us_trends, indent=1)

f1 = codecs.open("trend1.txt", encoding='utf-8', mode="w")

# print(seoul_trends)
f1.write(name1)
# f1.write(name1)
# f_us.write(us_trends)
#f_names=open('korea_names.txt', 'w')

# print world_trends
# print
# print us_trends

# print(korea_trends)
#file.write(unicode(json.dumps(korea_trends, indent=1)))

#file.write(json.dumps(korea_trends, indent=1).encode('utf-8'))
# file.close()
# f_us.close()
f1.close()
