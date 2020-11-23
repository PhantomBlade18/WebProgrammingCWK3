from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.http import QueryDict
from news.models import Category,Member,Article
import json

# Create your views here.

def registerUserView(request):
    if 'username' and 'password' and 'email' and 'dob' in request.POST:
        u = request.POST['username']
        p = request.POST['password']
        e = request.POST['email']
        d = request.POST['dob']
        user = Member(username=u,email = e, DOB = d)
        user.set_password(p)
        try: user.save()
        except IntegrityError: raise Http404('Username '+u+' already taken: Usernames must be unique')
        context = {
            'username' : u
        }
        return render(request,'news/index.html',context)

    else:
        raise Http404('POST data missing')

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request,'news/index.html', context)

def signup(request):
    context = {}
    return render(request,'news/register.html',context)
