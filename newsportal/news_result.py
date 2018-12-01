from newsapi import NewsApiClient
import rdflib


class NewsResult():

	# class attributes
	ontology_path = 'static/ontology/'
	# Init
	newsapi = NewsApiClient(api_key='572126b79fe04ce38c992297d4ac5752')

	def __init__(self):
		self.final_results = ''
		self.result_count = 0		


	def get_sources(self):
		sources = self.newsapi.get_sources()
		return sources
#	def get_headlines(self):

#	def get_everything(self):




#	def query(self,q):



#	def add_to_ontology(self,qquery_result, ontology='news.owl',isLocal=True):
#		g = rdflib.Graph()
#		if isLocal:
#			g.parse(self.ontology_path+ontology)
#		else:
#			g.parse(ontology)
#
#	def get_annotated_results(self,):




