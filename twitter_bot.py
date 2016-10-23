	# setup bot, listen, on recieving a new tweet: analyse and respond with 
	# 140 characters total
	# short version of claim (~105 characters for the claim)
	# short url of source https://t.co/66volBlLaF (23 characters for URL)
	# rating of claim: semi-true (9 characters max for rating)

class ReplyToTweet(StreamListener):

	def on_data(self, data):
		print data
		tweet = json.loads(data.strip())
        
		retweeted = tweet.get('retweeted')
		from_self = tweet.get('user',{}).get('id_str','') == account_user_id

		if retweeted is not None and not retweeted and not from_self:

			tweetId = tweet.get('id_str')
			screenName = tweet.get('user',{}).get('screen_name')
			tweetText = tweet.get('text')

			#chatResponse = chatbot.respond(tweetText)
			# Reply with factchecking content here

			replyText = '@' + screenName + ' ' + chatResponse

			#check if repsonse is over 140 char
			if len(replyText) > 140:
				replyText = replyText[0:139] + '…'

			print('Tweet ID: ' + tweetId)
			print('From: ' + screenName)
			print('Tweet Text: ' + tweetText)
			print('Reply Text: ' + replyText)

            # If rate limited, the status posts should be queued up and sent on an interval
			twitterApi.update_status(status=replyText, in_reply_to_status_id=tweetId)

if __name__ == '__main__':
	streamListener = ReplyToTweet()
	twitterStream = Stream(auth, streamListener)
	twitterStream.userstream(_with='user')