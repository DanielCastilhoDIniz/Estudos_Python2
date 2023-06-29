from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import tweepy
from pymongo import MongoClient


BRAZIL_WOE_ID = 23424768
auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# client = tweepy.Client(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

trends = api.get_place_trends(1)

for tweet in trends:
    print(tweepy)
