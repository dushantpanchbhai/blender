from django.shortcuts import render,redirect
from .models import Tutorial
from .models import Account

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def home(request):
    return render(request,'Main.html')

def login(request):
	if request.method=='POST':
		user = auth.authenticate(email=request.POST['Email'],password = request.POST['Password'])
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request,'login.html',{'error':'username or password is incorrect'})
	else:
		return render(request, 'login.html')



def signup(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username = request.POST['username'])
            return render(request,'signup.html',{'error':'Your username is taken'})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'],password=request.POST['password'], email=request.POST['email'])
            auth.login(request,user)
            return redirect('home')
    else:
        return render(request,'signup.html')


def models(request):
    return render(request,'models.html')

def tutorial(request):
    video = Tutorial.objects
    return render(request,'tutorial.html',{'video':video})