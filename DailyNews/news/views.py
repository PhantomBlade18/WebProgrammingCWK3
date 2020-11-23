from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.http import QueryDict
from news.models import Category
from news.models import Member
from news.models import Article
import json

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request,'news/index.html', context)

def registerMemberView(request):
    return render(request)
