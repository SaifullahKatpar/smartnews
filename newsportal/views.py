from django.shortcuts import render
from .news_result import NewsResult
# Create your views here.
def home(request):
	news_ob = NewsResult()
	result = news_ob.get_sources()
	return render(request,'newsportal/home.html',{'result':result['sources']})

#def news(request,q):
#	news_ob = NewsResult()
#	query_result = news_ob.query(q)
#	news_ob.add_to_ontology(query_result)

