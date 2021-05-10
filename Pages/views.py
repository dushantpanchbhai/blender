from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.
q="home"

def home(request):
    #if loop for adding user to database of analytics if new for email purpose
    if request.user.is_authenticated:
        print('-'*10,request.user.date_joined)
        if not Information.objects.filter(email=request.user.email).exists():
            p = Information(username = request.user.username,email=request.user.email,number=Information.objects.all().count()+1,Firstname=request.user.first_name,Lastname=request.user.last_name,join=request.user.date_joined,last_active=request.user.last_login)
            p.save()
        else:
            p = Information.objects.get(email=request.user.email)
            p.last_active = request.user.last_login
            p.save()
    video = Tutorial.objects.all()[:6]
    models= Models.objects.all()[:3]
    return render(request,'Main.html',{'video':video ,'models':models})

def login(request):
    global q
    if request.method=='POST':
        user = auth.authenticate(username =request.POST['username'],password =request.POST['password'])
        if user is not None:
            auth.login(request,user)
            if q!=None:
                print('going to previous page')
                if q=='http://127.0.0.1:8000/signup' or q=='http://127.0.0.1:8000/login':
                    return redirect('home')
                else:
                    #for saving email and password
                    if request.user.is_authenticated:
                        if not Information.objects.filter(email=request.user.email).exists():
                            p = Information(username = request.user.username,email=request.user.email,number=Information.objects.all().count()+1,Firstname=request.user.first_name,Lastname=request.user.last_name)
                            p.save()
                    return redirect(q)
            else:
                #print('not going to previous page')
                return redirect('home')
        return render(request,'login.html',{'error':'username or password is incorrect'})
    else:
        q=request.META.get('HTTP_REFERER')  ##used to get previous url of site
        return render(request, 'login.html')

def logout(request):
    print('we are in logout')
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        return render(request,'Main.html')

def signup(request, backend='django.contrib.auth.backends.ModelBackend'):
    global q
    if request.method == 'POST':
        try:
            user = User.objects.get(username = request.POST['username'])
            return render(request,'signup.html',{'error':'Your username is taken'})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'],password=request.POST['password'], email=request.POST['email'])
            auth.login(request,user)
            if q!=None:
                if q=='http://127.0.0.1:8000/signup' or q=='http://127.0.0.1:8000/login':
                    return redirect('home')
                else:
                    return redirect(q)
            else:
                return redirect('home')
    else:
        return render(request,'signup.html')

def models(request):
    if request.method == 'POST':
        a = Models.objects.get(pk=request.POST.get('j'))
        a.downloads = a.downloads +1
        redirect = a.link   
        a.save()
        return HttpResponseRedirect(redirect)
    models= Models.objects.order_by('-id')
    return render(request,'models.html',{'models':models})

def tutorial(request):
    video = Tutorial.objects.order_by('-id')
    return render(request,'tutorial.html',{'video':video})

def addmodel(request):
    if request.method == 'POST':
        form = ModelsForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data['title']
            if Models.objects.filter(title=data,link=form.cleaned_data['link']).exists():  
                print('item already exist')
                return HttpResponse('<h1> item already exist <h1>')
            form.save()
            form = ModelsForm()
            return render(request,'addmodel.html',{'form':form})
    else:
        form = ModelsForm()
        return render(request,'addmodel.html',{'form' : form})

def addvideo(request):
    if request.method == 'POST':
        form = VideosForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['title']
            if Tutorial.objects.filter(title=data,url=form.cleaned_data['url']).exists():
                print('item already exist')
                return HttpResponse('<h1> item already exist <h1>')
            form.save()
            form = VideosForm()
            return render(request,'addvideo.html',{'form':form})
    else:
        form = VideosForm()
        return render(request,'addvideo.html',{'form' : form})

def feedback(request):
    if request.method == 'POST':
        form = GeeksForm(request.POST)
        if form.is_valid():
            obj = Feedback()
            obj.email = form.cleaned_data['email']
            obj.website_rating = form.cleaned_data['website_rating']
            obj.artwork_rating = form.cleaned_data['artwork_rating']
            obj.youtube_rating = form.cleaned_data['youtube_rating']
            obj.feedback = form.cleaned_data['feedback']
            obj.save()
            return redirect('home')
        else:
            return render(request, 'feedback.html',{'form':form})
    form = GeeksForm()
    return render(request,'feedback.html',{'form':form})

def help(request):
    return render(request,'help.html')

def analytics(request):
    Info = Information.objects.order_by('-id')  
    feedback = Feedback.objects.order_by('-id')
    models = Models.objects.order_by('-id')   
    return render(request,'analytics.html',{'info':Info,'feedback':feedback,'models':models})
