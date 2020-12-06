from django.http import HttpResponse,Http404,JsonResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import QueryDict
from news.models import Category,Member,Article,Comment
from django.core.mail import send_mail
from DailyNews.settings import EMAIL_HOST_USER
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
        user = Member(username = u, email = e, DOB = d)
        user.set_password(p)
        try: user.save()
        except IntegrityError: raise Http404('Username ' +u+' already taken: Usernames must be unique')
        articles = Article.objects.all()
        categories = Category.objects.all()
        request.session['username'] = u
        request.session['password'] = p
        subject = 'Welcome to DailyNews!'
        message = 'Welcome, ' + u + '! Thank you for signing up to DailyNews!'
        send_mail(subject, message, EMAIL_HOST_USER, [e], fail_silently = False)
        context = {
            'username' : u,
            'articles': articles ,
            'categories':categories,
            'loggedin': True
        }
        return render(request,'news/index.html',context)

    else:
        raise Http404('POST data missing')

def login(request):
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
            context = {'articles': articles , 'categories':categories,'user': member ,'loggedin': True}
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
        user = Member.objects.get(username = request.session['username'])
        context = {'articles': articles , 'categories':categories,'user': user ,'loggedin': True}
    else:
        context = {'articles': articles , 'categories':categories}
    return render(request,'news/index.html', context)

def signup(request):
    return render(request,'news/register.html')

@loggedin
def viewProfile(request, user):
    username = request.session['username']
    categories = Category.objects.all()
    context = {'user': user, 'loggedin': True, 'member': user, 'categories': categories}
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
        raise Http404("Something went wrong. Figure it out")

@loggedin
def updateEmail(request, user):
    if request.method == "POST":
        email = request.POST['email']
        user.email = email
        user.save()
        username = request.session['username']
        categories = Category.objects.all()
        context = {'username': username, 'loggedin': True, 'member': user, 'categories': categories}
        return render(request, 'news/profile.html', context)
    else:
        raise Http404("Something went wrong.")

@loggedin
def updatePassword(request, user):
    if request.method == "POST":
        cpassword = request.POST['currentPassword']
        npassword = request.POST['newPassword']
        if user.check_password(cpassword):
            user.set_password(npassword)
            user.save()
            username = request.session['username']
            categories = Category.objects.all()
            context = {'successful': True , 'message': "Password Updated Successfully!"}
            return JsonResponse(context)
        else:
            context = {'successful': False , 'message': "The current password is incorrect!"}
            return JsonResponse(context)
    else:
        raise Http404("Something went wrong.")

@loggedin
def updateImage(request, user):
    if 'img_file' in request.FILES:
        image_file = request.FILES['img_file']
        user.profile_pic = image_file
        user.save()
        username = request.session['username']
        categories = Category.objects.all()
        context = {'username': username, 'loggedin': True, 'member': user, 'categories': categories}
        return render(request, 'news/profile.html', context)
    else:
        raise Http404('Image file not received')

@loggedin
def removeImage(request, user):
    user.profile_pic.delete()
    username = request.session['username']
    categories = Category.objects.all()
    context = {'username': username, 'loggedin': True, 'member': user, 'categories': categories}
    return render(request, 'news/profile.html', context)

@loggedin
def myNews(request,user):
    articles = Article.objects.order_by('-pub_Date')
    print("Hello World")
    print(user.favouriteCats.all())
    if 'username' in request.session:
        context = {'articles': articles ,'user':user,'username': request.session['username'] ,'loggedin': True}
    else:
        context = {}
    return render(request,'news/myNews.html', context)

def signup(request):
    return render(request,'news/register.html')

@loggedin
def LikeArticle(request,user):
    print(request.POST.get('aid'))
    id = request.POST.get('aid')
    article = get_object_or_404(Article, pk= id )
    if article.likes.filter(username = user.get_username()).exists():
        article.likes.remove(user)
        context = {'liked': False}
        print("Deleted")
    else:
        article.likes.add(user)
        context = {'liked': True}
        print("Added")

    return JsonResponse(context)

#Add Comment/reply
@loggedin
def addComment(request,user):
    if 'aid' and 'text'  in request.POST :
            print(request.POST['aid'])
            aid = request.POST['aid']
            body = request.POST['text']
            a = Article.objects.get(pk=aid)
            comment = Comment(article=a,author=user,text=body)
            comment.save()
            context= {
                'id':comment.id,
                'text':body,
                'author': comment.author.username
                }
            return JsonResponse(context)
    else:
        raise Http404("Missing Information in Form")

@loggedin
def addReply(request,user):
    if 'cid' and 'text'  in request.POST :
            cid = request.POST['cid']
            body = request.POST['text']
            c =Comment.objects.get(pk=cid)
            rep = Comment(author=user,reply= c, text=body)
            rep.save()
            context= {
                'id':rep.id,
                'text':body,
                'author': rep.author.username
                }
            return JsonResponse(context)
    else:
        raise Http404("Missing Information in Form")

#Delete comment/reply
@loggedin
def deleteComment(request,user):
    if request.method=="DELETE":
        data = QueryDict(request.body)
        id = data.get('cid')
        comment = Comment.objects.get(pk = id)
        comment.delete()
        return HttpResponse("")
    else:
        raise Http404("Invalid Request")
@loggedin
def deleteReply(request,user):
    if request.method=="DELETE":
        data = QueryDict(request.body)
        id = data.get('rid')
        comment = Comment.objects.get(pk = id)
        comment.delete()
        return HttpResponse("")
    else:
        raise Http404("Invalid Request")

#Update comment/reply
@loggedin
def updateComment(request,user):
    if request.method=="PUT":
        data = QueryDict(request.body)
        id = data.get('cid')
        body =data.get('text')
        comment = Comment.objects.get(pk = id)
        comment.text = body
        comment.save()
        context = {'text': comment.text}
        return JsonResponse(context)
    else:
        raise Http404("Invalid Request")
