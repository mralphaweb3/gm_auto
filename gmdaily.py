import os
import tweepy

# Fetch API keys from GitHub Secrets
api_key = os.environ["X_API_KEY"]
api_secret = os.environ["X_API_SECRET"]
access_token = os.environ["X_ACCESS_TOKEN"]
access_token_secret = os.environ["X_ACCESS_TOKEN_SECRET"]

# Connect to Twitter API v2
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Send the tweet
try:
    response = client.create_tweet(text="gm ☀️")
    print("Tweet sent successfully!")
except Exception as e:
    print(f"Error: {e}")
