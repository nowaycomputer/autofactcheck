import tweepy

# Wrapper class to provide access to twitter
class Twitter_Access:	
	def __init__(self):
		con_key = open('.twitter_con_key').read()
		con_sec = open('.twitter_con_sec').read()
		acc_key = open('.twitter_acc_key').read()
		acc_sec = open('.twitter_acc_sec').read()

		self.auth = tweepy.OAuthHandler(con_key, con_sec)
		self.auth.set_access_token(acc_key, acc_sec)

		self.api = tweepy.API(self.auth)

	# Search twitter for something
	def search_twitter(self,query):
		results = self.api.search(q=query)
		result_text=[]
		for result in results:
			result_text.append(result.text)
		return result_text

# A class for a twitter bot that will attempt to determine the veracity of a fact (fact check style)
# Work in progress in every sense
class Twitter_Bot:
	def __init__(self):

		con_key = open('.twitter_con_key').read()
		con_sec = open('.twitter_con_sec').read()
		acc_key = open('.twitter_acc_key').read()
		acc_sec = open('.twitter_acc_sec').read()

		self.auth = tweepy.OAuthHandler(con_key, con_sec)
		self.auth.set_access_token(acc_key, acc_sec)

		self.api = tweepy.API(self.auth)

