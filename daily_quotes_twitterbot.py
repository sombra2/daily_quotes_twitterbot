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
client = tweepy.Client(
                    bearer_token=credentials.bearer_token,
                    consumer_key=credentials.consumer_key,
                    consumer_secret=credentials.consumer_secret,
                    access_token=credentials.access_token,
                    access_token_secret=credentials.access_token_secret
                    )


# sending the tweet
client.create_tweet(text = quote + ' #DailyQuote')