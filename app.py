# main access point for fact checker
import wikipedia as wiki
import twitter_trawling as twitter
import google_kt as google
import text_analysis as text_an
import csv

ta=text_an.Text_Analyser()

# Very basic identification of claim types
with open('sampledata.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	next(reader)
	claim_types={}
	number_of_numerical=0
	for row in reader:
		#count the claim types
		if row[1] in claim_types:
			claim_types[row[1]]=claim_types[row[1]]+1
		else:
			claim_types[row[1]]=1
		claim=row[3]

		#print claim
		# Work out if claim is numerical
		# CD: numeral, cardinal
		# JJR: adjective, comparative
		CD_instances=ta.check_for_type(claim,'CD')
		JJR_instances=ta.check_for_type(claim,'JJR')
		#subjects=ta.get_subject(claim)
		if len(CD_instances)>0 or len(JJR_instances)>0:
			print claim
			number_of_numerical=number_of_numerical+1
			
			if len(CD_instances)>0:
				print ta.check_for_type(claim,'CD')
			if len(JJR_instances)>0:
				print ta.check_for_type(claim,'JJR')
			ta.extract_entities(claim)



	print "Number of numerical",number_of_numerical
	print claim_types
		# quote

		# properties

		# position
		# VBD: verb, past tense

		# Work out if claim is 
		#print ta.get_nouns(claim)

		
