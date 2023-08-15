# Daily Quote Twitter Bot

This is a simple Python script that tweets a random quote from a provided list of quotes every day using the Twitter API. The bot is built using the Tweepy library and authenticates using the provided credentials.

## Features

- Tweets a random quote daily with the hashtag #DailyQuote.
- Uses the Tweepy library for easy interaction with the Twitter API.
- Quotes are sourced from a file (`all_quotes.txt`).
- Secure authentication using credentials stored in a separate `credentials.py` file.

## Prerequisites

Before using the bot, you need to set up your Twitter Developer account and obtain the necessary API keys and tokens. Store these credentials in the `credentials.py` file in the following format:

```python
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
bearer_token = 'your_bearer_token'
