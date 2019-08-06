!pip install pandas 
!pip install tweepy
!pip install vaderSentiment


import tweepy
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer


#My Twitter API Authentication Variables
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = api.search('Artificial Intelligence', count=200)

data = pd.Dataframe(data=[tweet.text for tweet in tweets], columns=['Tweets'])

display(data.head(10))

print(tweets[0].created_at)


import nltk
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

listy = []

for index, row in data.iterrows():
  ss = sid.polarity_scores(row["Tweets"])
  listy.append(ss)
  
se = pd.Series(listy)
data['polarity'] = se.values

dislay(data.head(100))