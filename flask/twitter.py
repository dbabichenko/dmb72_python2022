'''
Working with Twitter API
This tutorial is based on examples provided at https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/

For this tutorial you will need to register for a Twitter developer account and obtain Twitter API keys (https://developer.twitter.com/en).

To access the Twitter API, you will need 4 things from the your Twitter App page. These keys are located in your Twitter app settings in the Keys and Access Tokens tab.

consumer key
consumer seceret key
access token key
access token secret key
This version of the tutorial is using your instructor's API keys - please make sure to replace them with your own keys if you want to experiment with this code

You will also need to install the tweepy module using one of the following commands:

pip install tweepy
pip3 install tweepy
conda install tweepy
'''

import os
import tweepy as tw

# Define your twitter API keys
consumer_key= 'yourkeyhere'
consumer_secret= 'yourkeyhere'
access_token= 'yourkeyhere'
access_token_secret= 'yourkeyhere'

# These are your instructor's keys - if you are planning on experimenting with this code
# please delete this entire block and use your own keys in the code block above
consumer_key = '3tvxSM7Of1giPWxngUjDiatkd'
consumer_secret = 'AZUsaWnMaUYXLcrNS74sLD0p9za2GzL0LpgrZIUGn3Zk5UrFrz'
access_token = '63175705-PdeWIim8wJUskrAFVHfGPwJ2wKRREaZGWzo74TIZx'
access_token_secret = '1jYdgoDFN6WA5rOrp4VL0GQicvMJiwVybVkQXWTlwPW1l'


# Connect to twitter API:
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "#vaccine"

'''
.Cursor() returns an object that you can iterate or loop over to access the data collected. Each item in the iterator has various attributes that you can access to get information about each tweet including:

the text of the tweet
who sent the tweet
the date the tweet was sent
... and more
The code below loops through the object and prints the text associated with each tweet.
'''

try:
    # Collect tweets
    tweets = tw.Cursor(api.search_tweets,
            q=search_words,
            lang='en').items()
except tw.TweepyException as e:
    if e == "[{u'message': u'Rate limit exceeded', u'code': 88}]":
        print(e)
        time.sleep(60*5) #Sleep for 5 minutes
    else:
        print(e)

# Iterate and print tweets
for tweet in tweets:
    print(tweet)
    break;