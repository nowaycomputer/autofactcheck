from nltk.tag import pos_tag

# Class for analysing text with NLTK
class Text_Analyser:

	# A simple function to extract nouns from text for the purposes of searching
	def check_for_type(self,text,type):
		tagged_sent = pos_tag(text.split())
		type_instances = [word for word,pos in tagged_sent if pos == type]
		return type_instances
