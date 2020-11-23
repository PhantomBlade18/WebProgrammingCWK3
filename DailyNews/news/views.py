from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.http import QueryDict
from news.models import Category,Member,Article
import json

# Create your views here.

def registerUserView(request):
    return render(request)

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request,'news/index.html', context)
