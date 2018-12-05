from newsapi import NewsApiClient


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

	def get_headlines_from_source(self,source):
		print(source)
		top_headlines = self.newsapi.get_top_headlines(sources=source)
		return top_headlines['articles']

	# return headlines from country 

	def add_to_ontology(self,query_result, ontology='news.owl',isLocal=True):
		
		
		



