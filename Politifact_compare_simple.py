import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))

def tf_idf_cosine_comparison (raw_text):
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform(raw_text)
    return (tfidf * tfidf.T).A[0,1]

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        if item not in stop:
            stemmed.append(stemmer.stem(item))
    return stemmed

def tokenise(text, stem=False):
    stemmer = PorterStemmer()
    tokens = nltk.word_tokenize(text)
    if stem:
        tokens = stem_tokens(tokens, stemmer)
    return tokens

def politifact_match():
    highest_score = 0
    closest_match = {}
    for story in politifact_filtered:
        politifact_claim = story['claim']
        politifact_tokens = tokenise(politifact_claim, True)
        politifact_token_string = " ".join(politifact_tokens)
        similarity_score = tf_idf_cosine_comparison([claim_token_string, politifact_token_string])
        if similarity_score > highest_score:
            highest_score = similarity_score
            closest_match = story
    return closest_match, highest_score
    

claim = "400 Americans are richer than half of the rest of the country"
claim_tokens = tokenise(claim, True)
claim_token_string = " ".join(claim_tokens)

with open('data/politifact_filtered.json', 'r') as data_file:
    politifact_filtered = json.load(data_file)

closest_match, highest_score = politifact_match()


print(closest_match['claim'], "score:", highest_score)
