import tweepy
from textblob import TextBlob

# Replace 'YOUR_API_KEY', 'YOUR_API_SECRET_KEY', 'YOUR_ACCESS_TOKEN', and 'YOUR_ACCESS_TOKEN_SECRET'
# with your own Twitter API credentials
api_key = 'YOUR_API_KEY'
api_secret_key = 'YOUR_API_SECRET_KEY'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

def authenticate_twitter():
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

def analyze_sentiment(tweet_text):
    analysis = TextBlob(tweet_text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

if __name__ == "__main__":
    topic = input("Enter the topic or hashtag to analyze: ")
    tweet_count = int(input("Enter the number of tweets to analyze: "))

    api = authenticate_twitter()
    tweets = api.search_tweets(q=topic, lang="en", count=tweet_count)

    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for tweet in tweets:
        sentiment = analyze_sentiment(tweet.text)
        if sentiment == "positive":
            positive_count += 1
        elif sentiment == "negative":
            negative_count += 1
        else:
            neutral_count += 1

    total_count = positive_count + negative_count + neutral_count

    print("\nSentiment Analysis Results:")
    print(f"Positive Tweets: {positive_count} ({(positive_count / total_count) * 100:.2f}%)")
    print(f"Negative Tweets: {negative_count} ({(negative_count / total_count) * 100:.2f}%)")
    print(f"Neutral Tweets: {neutral_count} ({(neutral_count / total_count) * 100:.2f}%)")