This is a Twitter bot developed in Python that allows you to tweet content from a text file.

## Requirements

- Python 3.x installed
- Python package: tweepy

## Usage

1- Open the twitterbot.py file in a code editor.

2- Modify the login credentials in the code with your own Twitter API keys:

   consumer_key = "YOUR_CONSUMER_KEY"
   consumer_secret = "YOUR_CONSUMER_SECRET"
   access_token = "YOUR_ACCESS_TOKEN"
   access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
   bearer_token = "YOUR_BEARER_TOKEN"

3- Make sure to correctly place the path to the txt file containing the tweets. 

4- Make sure that the tweets.txt file contains the tweets you want to publish, separated by semicolon (;).


5- Execute the `twitterbot.py` script using the following command: `python twitterbot.py`


The bot will read the tweets.txt file and publish each tweet on Twitter. We expect a time of 10 seconds between each tweet. We can modify the time between tweet and tweet by modifying the time.sleep(Number of seconds we want to pass between tweet and tweet).

## Reminders

Make sure to replace the YOUR_CONSUMER_KEY, YOUR_CONSUMER_SECRET, YOUR_ACCESS_TOKEN, YOUR_ACCESS_TOKEN_SECRET and YOUR_BEARER_TOKEN sections with your relevant Twitter API access keys. Also, verify that the separation of tweets in the `tweets.txt` file is actually using semicolon (`;`) as indicated in the code.
