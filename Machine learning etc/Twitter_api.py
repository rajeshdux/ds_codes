from tweepy import API
from tweepy import Cursor
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import numpy as np
import pandas as pd
from textblob import TextBlob
import re
import matplotlib.pyplot as plt

####### Twitter  Stream Listener ##############3
class Twitterlistener(StreamListener):
# Basic listener class that prints out the tweets to stdout and to a file..

    def __init__(self, ftfile):
        self.ftfile = ftfile

    def on_data(self, data):
        try:
            print(data)
            with open(self.ftfile, 'a') as file:
                file.write(data)
                return True
        except BaseException as e:
            print('Error on data: %s', str(e))

    def on_error(self, status):
        if status == 420:
            # Returning false in case of data limits occur..
            return False
        print (status)

###### Twitter Authenticator ##############
class twitter_authenticator():
    def authenticator_app(self):
        # consumer key, consumer secret, access token, access secret.
        ckey = "BJLMbUq7au6lFeNQF4QO2ZQsa"
        csecret = "a8v40HFNf5virM6dn1PDpw2HDtPXg53zRJ6ZQpzcWGVn8QEjZS"
        atoken = "1385264515-lwIlfXy8vTFG1rYfgON4MRtDpSCrK9F6deEuRio"
        asecret = "HFi76cndRAQYcoOU0Uy1evPw3V7P4HElGNU0jFkaCbOMF"

        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        return auth

######## Twitter Streamer #############
class twitter_streamer():
# Class for processing and streaming live tweetts

    def __init__(self):
        self.twitter_authenticator = twitter_authenticator()

    def stream_tweets(self, ftfile, hashtaglist):
    # This handles authentication and connection to twitter  streaming API..
        listener = Twitterlistener(ftfile)
        auth = self.twitter_authenticator.authenticator_app()
        twitterStream = Stream(auth, listener)
        twitterStream.filter(track = hashtaglist)

###### Twitter Client #########
class twitter_client():
    def __init__(self, twitter_user=None):
        t = twitter_authenticator()
        self.auth = t.authenticator_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_timeline_tweets(self, num_tweets):
        tweets = []
        for i in Cursor(self. twitter_client.user_timeline, id = self.twitter_user).items(num_tweets):
            tweets.append(i)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for i in Cursor(self.twitter_client.friends, id = self.twitter_user).items(num_friends):
            friend_list.append(i)
        return friend_list

    def get_timeline_tweets(self, num_tweets):
        timeline_tweets = []
        for i in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            timeline_tweets.append(i)
        return timeline_tweets

class tweetAnalyzer():
    """
    funcitonality for analyzing and categorizing content from tweets.
    """
    def clean_tweet(self,tweets):
        return ' '.join(re.sub("@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|([\w+\/\/\S+]", " ", tweets).split())

    def analyze_sentiment(self, tweets):
        analysis = TextBlob(self.clean_tweet(tweets))
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    def tweets_to_dataframe(self, tweets):

        df = pd.DataFrame()
        # df['Id'] = np.array([i.id for i in tweets])
        # df['IdStr'] = np.array([i.id_str for i in tweets])
        # df['User'] = np.array([i.user for i in tweets])
        df['Tweets_data'] = np.array([i.text for i in tweets])
        # df['Contributors'] = np.array([i.contributors for i in tweets])
        # df['Truncated'] = np.array([i.truncated for i in tweets])
        # df['Lang'] = np.array([i.lang for i in tweets])
        # df['Place'] = np.array([i.place for i in tweets])
        # df['Geo'] = np.array([i.geo for i in tweets])
        # df['Retweet'] = np.array([i.retweet for i in tweets])
        # df['Retweets'] = np.array([i.retweets for i in tweets])
        # df['RetweetCount'] = np.array([i.retweet_count for i in tweets])
        # df['Parse'] = np.array([i.parse for i in tweets])
        # df['ParseList'] = np.array([i.parse_list for i in tweets])
        # df['IdLength'] = np.array([len(str(i.id)) for i in tweets])
        # df['Date'] = np.array([i.created_at for i in tweets])
        # df['Source'] = np.array([i.source for i in tweets])
        # df['SourceURL'] = np.array([i.source_url for i in tweets])
        # df['Likes'] = np.array([i.favorite for i in tweets])
        # df['Liked'] = np.array([i.favorite for i in tweets])
        # df['Likes_count'] = np.array([i.favorite_count for i in tweets])
        # df['Author'] = np.array([i.author for i in tweets])
        # df['IRT_StatusId'] = np.array([i.in_reply_to_status_id for i in tweets])
        # df['IRT_UserId'] = np.array([i.in_reply_to_user_id for i in tweets])
        # df['IsQuoteStatus'] = np.array([i.is_quote_status for i in tweets])
        # df['Destroyed'] = np.array([i.destroy for i in tweets])
        return df


if __name__ == '__main__':
    t_client = twitter_client()
    t_analyzer = tweetAnalyzer()
    api = t_client.get_twitter_client_api()
    tweets = api.user_timeline(screen_name="Nayantara", count=30)

# prints the tweet in the beginning.....
    # print(tweets[0].text)

#prints the list of APIs available for the tweet.........
    # print(dir(tweets[0]))

# DataFrame..................
    df = t_analyzer.tweets_to_dataframe(tweets)

# loop through the tweets............
#     for i in tweets:
#         print(i.place)
#
# first 10 tweets............
#     print(df.head(10))
#
# some queries..............
#     print(np.mean(df['IdLength']))
#     print(df['Likes_count'])
#     print(df['RetweetCount'])
#     print(df['Author'])
#     print(df['Data'])
#
# plotting Graph...................
#     likescount = pd.Series(data= df['Likes_count'].values, index=df['Date'])
#     likescount.plot(figsize=(16, 4), color='r')
#     plt.show()
#
#     RetweetsS = pd.Series(data=df['RetweetCount'].values, index=df['Date'])
#     RetweetsS.plot(figsize=(16, 4), color='r')
#     plt.show()
#
# plotting Dual Graph..............
#     likes_count = pd.Series(data= df['Likes_count'].values, index=df['Date'])
#     likes_count.plot(figsize=(16, 4), label='Likes', legend=True)
#
#     Retweets_S = pd.Series(data=df['RetweetCount'].values, index=df['Date'])
#     Retweets_S.plot(figsize=(16, 4), label='Retweets', legend=True)
#
#     plt.show()
#
######## Sentiment Analysis ##################

    df['Sentiment'] = np.array([tweetAnalyzer.analyze_sentiment(i) for i in df['Tweets_data']])
    print(df.head(10))
