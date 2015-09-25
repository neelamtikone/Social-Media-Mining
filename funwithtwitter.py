
from __future__ import absolute_import, print_function
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

import pandas as pd
import json


import matplotlib.pyplot as plt

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="yyEyYLArDiGsXlCm3Xqob65hu"
consumer_secret="jTSodfT5yDJpHMwjbUKG4NiOWI0tT2NhGiuzBxjyQeNyWzAG4D"


# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="3631558032-Jaf8hK7bH3YLRN1QHPQd82ejyWkkG3SnCxCtoyo"
access_token_secret="S5b4Ak3WOQjj4Z8sVor1CvsypRxhiPTcJ63Wd0Wuwbdxo"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)



if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #stream = Stream(auth, l)
    #stream.filter(track=['car'])


api=tweepy.API(auth)
results=api.search(q="bengali")


'''to inspect results'''
'''
def print_tweet(tweet):
    print(tweet.user.screen_name,tweet.user.name,tweet.created_at)
    print (tweet.text)

tweet=results[5]
print_tweet(tweet)
'''

'''to inspect status'''
'''
tweet=results[2]
for param in dir(tweet):
    if not param.startswith("_"):
        print(param,eval("tweet."+param))
'''

'''to inspect author'''
'''tweet=results[3]
user=tweet.author

for param in dir(user):
    if not param.startswith("_"):
        print(param,eval("user."+param))
'''
'''using cursor for Pagination'''
''''
crap=[]
for tweet in tweepy.Cursor(api.search,q="bengali").items(100):
    crap.append(tweet)

print (len(crap))
'''''
''' store result in dataframe
def process_results(results):
    id_list=[tweet.id for tweet in results]
    data_set= pd.DataFrame(id_list, columns=["id"])

    data_set["text"]=[tweet.text for tweet in results]
    data_set["created_at"]=[tweet.created_at for tweet in results]
    data_set["retweet_count"]=[tweet.retweet_count for tweet in results]
    data_set["created_at"]=[tweet.created_at for tweet in results]
    data_set["favorite_count"]=[tweet.favorite_count for tweet in results]
    data_set["source"]=[tweet.source for tweet in results]
    return data_set
data_set=process_results(results)

data_set.head(5)
'''
top10 = api.trends_place(id=2473224)

print (top10)

user = api.get_user('myTwitter')
print ("Retreiving friends for", user.screen_name)
for friend in tweepy.Cursor(api.friends).items():
    print ("\n", friend.screen_name)'''
    
    
def process_friend(friend):
    
    print(friend.screen_name, '\t', friend.id)
    print(friend.id)
    print(friend.timeline,'\n').items(10)

for friend in tweepy.Cursor(api.friends).items(25):
    process_friend(friend)
