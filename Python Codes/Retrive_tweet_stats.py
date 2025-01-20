import tweepy

# Replace these with your actual Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_tweet_info(tweet_id):
    try:
        tweet = api.get_status(tweet_id, tweet_mode='extended')  # Use tweet_mode='extended' to get full tweet text

        tweet_text = tweet.full_text
        retweets_count = tweet.retweet_count
        favorites_count = tweet.favorite_count

        return {
            'tweet_text': tweet_text,
            'retweets_count': retweets_count,
            'favorites_count': favorites_count
        }
    except tweepy.TweepError as e:
        return {'error': str(e)}

tweet_id = 'YOUR_TWEET_ID'  # Replace with the actual tweet ID
tweet_info = get_tweet_info(tweet_id)

if 'error' in tweet_info:
    print(f"An error occurred: {tweet_info['error']}")
else:
    print("Tweet Text:", tweet_info['tweet_text'])
    print("Retweets Count:", tweet_info['retweets_count'])
    print("Favorites Count:", tweet_info['favorites_count'])
