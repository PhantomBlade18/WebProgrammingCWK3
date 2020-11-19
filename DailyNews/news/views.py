from django.shortcuts import render
from .models import Category, Article

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request,'news/index.html', context)
