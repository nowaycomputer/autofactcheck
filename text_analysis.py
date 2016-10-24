import nltk
import re

# Class for analysing text with NLTK
class Text_Analyser:

	def __init__(self):
		years_to_ignore=range(1900,2017,1)
		self.string_years=[]
		for year in years_to_ignore:
			self.string_years.append(str(year))
	# A simple function to extract nouns from text for the purposes of searching
	def check_for_type(self,text,type):
		tagged_sent = nltk.pos_tag(text.split())
		type_instances = [word for word,pos in tagged_sent if pos == type]
		for instance in type_instances:
			if re.sub('[^A-Za-z0-9]+', '', instance) in self.string_years:
				type_instances.remove(instance)
		return type_instances

	def get_subject(self,text):
		tagged_sent = nltk.pos_tag(text.split())
		type_instances = [word for word,pos in tagged_sent if pos == 'NN']
		for sent in nltk.sent_tokenize(text):
				tokens = nltk.tokenize.word_tokenize(sent)
				tags = nltk.pos_tag(tokens)
				print tags
				# for tag in tags:
				# 	if tag[1]=='PERSON': 
				# 		print tag

		return type_instances

	def extract_entities(self,text):
		entities=[]
		for sent in nltk.sent_tokenize(text):
			for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
				if len(chunk):
					if 'GPE' in str(chunk):
						results= str(chunk[0]).replace("(","").replace(")","").replace("'", "").split(',')
						entities.append(results[0])
		return entities
				# if hasattr(chunk, 'node'):
				#  	for c in chunk.leaves():
				#  		if c[0] is 'GPE':
				#  			print c
				# 		if 'GPE' in c:
				# 			print c	
					#print chunk.node, ' '.join(c[0] for c in chunk.leaves())

