from django.http import HttpResponse,Http404,JsonResponse
from django.template import loader
from django.shortcuts import render
from django.http import QueryDict
from news.models import Category,Member,Article
import json

def loggedin(view):
    ''' Decorator that tests whether user is logged in '''
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try: user = Member.objects.get(username=username)
            except Member.DoesNotExist: raise Http404('Member does not exist')
            return view(request, user)
        else:
            return render(request,'news/login.html')
    return mod_view

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
        articles = Article.objects.all()
        categories = Category.objects.all()
        request.session['username'] = username
        request.session['password'] = password
        context = {
            'username' : u,
            'articles': articles ,
            'categories':categories,
            'loggedin': True
        }
        return render(request,'news/index.html',context)

    else:
        raise Http404('POST data missing')

def login(request):    #HOOK THIS UP TO JS SO THAT IT IS AN AJAX YER CRETIN (Speaking to you Jakub)
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
            articles = Article.objects.all()
            categories = Category.objects.all()
            context = {'articles': articles , 'categories':categories,'username': username ,'loggedin': True}
            return render(request, 'news/index.html', context)
        else:
            raise Http404("Username or Password is Incorrect")

@loggedin
def logout(request, user):
    request.session.flush()
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {'articles': articles , 'categories':categories}
    return render(request,'news/index.html', context)


def index(request):

    articles = Article.objects.all()
    categories = Category.objects.all()
    if 'username' in request.session:
        context = {'articles': articles , 'categories':categories,'username': request.session['username'] ,'loggedin': True}
    else:
        context = {'articles': articles , 'categories':categories}
    return render(request,'news/index.html', context)

def signup(request):
    return render(request,'news/register.html')


@loggedin
def viewProfile(request, user):
    username = request.session['username']
    categories = Category.objects.all()
    context = {'username': username, 'loggedin': True, 'member': user, 'categories': categories}
    return render(request, 'news/profile.html', context)

@loggedin
def updateCategory(request,user):
    if request.method == "PUT":
        data = QueryDict(request.body)
        catName = data.get('catName')
        category = Category.objects.get(name = catName)
        user.favouriteCats.add(category)
        user.save()
        return HttpResponse("")

    elif request.method=="DELETE":
        data = QueryDict(request.body)
        catName = data.get('catName')
        category = Category.objects.get(name = catName)
        user.favouriteCats.remove(category)
        user.save()
        return HttpResponse("")
    else:
        raise Http404("Something went wrong. figure it out")

@loggedin
def updateImage(request, user):
    if 'img_file' in request.FILES:
        image_file = request.FILES['img_file']
        user.profile_pic = image_file
        user.save()
        return HttpResponse(user.profile_pic.url)
    else:
        raise Http404('Image file not received')



#Helper Methods

#JAKUBS THINGS TO DO AFTER WORK: IGNORE IF NOT JAKUB
