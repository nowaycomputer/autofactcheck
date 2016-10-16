import json
import urllib

# A wrapper class for querying Google's knowledge tree and hacked together functions
class Google_Knowledge_Tree:
    def __init__(self):
        self.api_key = open('.api_key').read()
        self.service_url = 'https://kgsearch.googleapis.com/v1/entities:search'

    # takes a text name and searches the google knowledge tree for the top hit
    # then returns the url of their wikipedia page and their schema.org id
    def find_person(self,query):
        params = {
            'query': query,
            'limit': 10,
            'indent': True,
            'key': self.api_key,
        }
        url = self.service_url + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read())
        #if 'Person' in response['itemListElement']['@type']:
        #    print 'person query!'
        wiki_url=''
        schema_id=''
        name=''
        for element in response['itemListElement']:
            if 'Person' in element['result']['@type']:
                wiki_url=element['result']['detailedDescription']['url']
                schema_id=element['result']['@id']
                name=element['result']['name']
                break # after the top hit
        return name,wiki_url, schema_id