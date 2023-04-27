from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
# def first(request):
#     return HttpResponse('hello world')


def home(request):
    return render(request,'home.html') 
    
def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'user name is alredy taken')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.info(request,'email is already taken')
            return redirect('signup')
        else:
            user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.set_password(password)
            user.save()
            messages.info(request,'successfully created')
            return redirect('signin')


    return render(request,"register.html")



def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Invalid username or password!")
            return redirect('signin')
    
    return render(request,"login.html")




def logout(request):
    auth.logout(request)
    messages.info(request,"You are signed out!!")
    return redirect('signin')