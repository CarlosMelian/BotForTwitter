
import tweepy
import time

# Configure access credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
bearer_token = "YOUR_BEARER_TOKEN"

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

# Read the content of the text file
with open('C:/Users/YOURPC/XXXX/XXXX/BotTwitter/tweets.txt.txt', 'r', encoding='utf-8') as f:
    tweets = f.read().split(';')

# Iterate on tweets and tweet them
for tweet in tweets:
    tweet = tweet.strip()
    if tweet:
        client.create_tweet(text=tweet)
        time.sleep(10)

