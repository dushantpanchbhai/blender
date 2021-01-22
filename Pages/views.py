from django.shortcuts import render,redirect
from .models import Tutorial
from .models import Account
from .models import Models

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
q="home"

def home(request):
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
                #print('going to previous page')
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

def signup(request):
    global q
    if request.method == 'POST':
        try:
            user = User.objects.get(username = request.POST['username'])
            return render(request,'signup.html',{'error':'Your username is taken'})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'],password=request.POST['password'], email=request.POST['email'])
            auth.login(request,user)
            if q!=None:
                return redirect(q)
            else:
                return redirect('home')
    else:
        return render(request,'signup.html')

def models(request):
    models= Models.objects
    return render(request,'models.html',{'models':models})

def tutorial(request):
    video = Tutorial.objects
    return render(request,'tutorial.html',{'video':video})