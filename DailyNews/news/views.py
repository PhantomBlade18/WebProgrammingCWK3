from django.http import HttpResponse,Http404,JsonResponse
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

def login(request):    #HOOK THIS UP TO JS SO THAT IT IS AN AJAX YER CRETIN (SPeaking to you Jakub)
    if  request.method == 'GET':
        return render(request,'news/login.html')
    elif not ('username' in request.POST and 'password' in request.POST) and request.method == 'POST':
        context = {
            'msg': "Please enter the username and password"
            }
        data = json.dumps(context)
        return JsonResponse(data)
    else:
        username = request.POST['username']
        password = request.POST['password']
        try: member = Member.objects.get(username=username)
        except Member.DoesNotExist: raise Http404('User does not exist')
        if member.check_password(password):
            # remember user in session variable
            request.session['username'] = username
            request.session['password'] = password
            context = {
               'username': username,
            }
            return render(request, 'news/index.html', context)
        else: 
            raise Http404("Username or Password is Incorrect")

def loggedin(view): #NOTE FOR JAKUB!!! WORK ON THIS YER BLOODY CRETIN
    ''' Decorator that tests whether user is logged in '''
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try: user = Member.objects.get(username=username)
            except Member.DoesNotExist: raise Http404('Member does not exist')
            return view(request, user)
        else:
            return render(request,'mainapp/not-logged-in.html',{})
    return mod_view

@loggedin
def logout(request, user):
    request.session.flush()
    context = { 'appname': appname }
    return render(request,'mainapp/logout.html', context)

def loggedin(view): #NOTE FOR JAKUB!!! WORK ON THIS YER BLOODY CRETIN
    ''' Decorator that tests whether user is logged in '''
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try: user = Member.objects.get(username=username)
            except Member.DoesNotExist: raise Http404('Member does not exist')
            return view(request, user)
        else:
            return render(request,'mainapp/not-logged-in.html',{})
    return mod_view


def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request,'news/index.html', context)

def signup(request):
    return render(request,'news/register.html')
