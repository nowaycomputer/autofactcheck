
from bs4 import BeautifulSoup
import requests

class Wikipedia

	def __init__(self):
		self.base__wiki_url='https://en.wikipedia.org/wiki/'

	# a function that searches for a given word or phrase and returns the paragraph or block of text within
	# which it is contained on wiki	
	def search_for_term(url,term):
		respond = requests.get(url)
		soup = BeautifulSoup(respond.text)
		content_text = soup.find(id="content").text
		# if phrase is found
		if term in content_text:
			print 'found'
    
url='https://en.wikipedia.org/wiki/Donald_Trump'
search_for_term(url,'global warming')


