from django.shortcuts import render
from .news_result import NewsResult
from django.http import HttpResponse
from .forms import QueryForm


def home(request):
	form = QueryForm()
	return render(request,'newsportal/home.html',{'form':form})

def news(request):
	if request.GET['source']:
		headlines = NewsResult().get_headlines_from_source(request.GET['source'])
	else:
		headlines = 'No Healines Available'

	return HttpResponse(headlines)

#def news(request,q):
#	news_ob = NewsResult()
#	query_result = news_ob.query(q)
#	news_ob.add_to_ontology(query_result)

