import tweepy
from textblob import TextBlob

consumer_key = 'FjS0tlQtxV03gCfiahgP8E9Sj'
consumer_secret = 'UiS61MUb5NN7JH1xyATPpfxkFMkpdbJN1UbSjHP1zVDwxs0OT1'

access_token = '204998940-ioILivM3KJxijHGX22zkoW2dEZmneztdg8Qr15qN' 
access_token_secret = 'GT672CIMRB9PAyNSHCdJuxVIz4hc5dxoLoumGnyMyCLbV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Murray Rothbard')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


