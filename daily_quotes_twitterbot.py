import tweepy
import random
import os
import credentials

cwd = os.path.dirname(os.path.realpath(__file__))

# first grab a random quote off the file

with open(cwd + '/all_quotes.txt', 'r') as f:
    quotes = f.read().splitlines()
    quote = random.choice(quotes)


# authentication in the Twitter API

consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# sending the tweet

api.update_status(status = quote + ' #DailyQuote')