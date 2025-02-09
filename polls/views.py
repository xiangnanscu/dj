from django.shortcuts import render

from django.db.models import Count
from django.http import HttpResponse
from polls.models import Author, Article

def index(request):
    query_str = request.GET.get('q', "Author.objects.annotate(article_count=Count('articles')).filter(article_count__gt=2)")
    queryset = eval(query_str)
    return HttpResponse(queryset.query)



# Create your views here.
