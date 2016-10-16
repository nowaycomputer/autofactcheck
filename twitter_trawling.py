import tweepy

class Twitter_Access:
	def __init__(self):

		con_key = open('.twitter_con_key').read()
		con_sec = open('.twitter_con_sec').read()
		acc_key = open('.twitter_acc_key').read()
		acc_sec = open('.twitter_acc_sec').read()

		self.auth = tweepy.OAuthHandler(con_key, con_sec)
		self.auth.set_access_token(acc_key, acc_sec)

		self.api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text