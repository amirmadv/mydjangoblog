from django.http.request import HttpRequest
from django.shortcuts import render , HttpResponse
from . import models

def articles_list(request):
    articles = models.Article.objects.all().order_by('date')

    return render(request,'articles/articleslist.html', {'articles':articles})

def articles_detail(request,slug):
    return HttpResponse(slug)

