from django.shortcuts import render, HttpResponse,redirect

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login , logout

from .models import cv
from .forms import cv_form

# Create your views here.

# cv.html output page
def my_cv(request):
    data=cv.objects.filter(user=request.user)
    
    language=[]
    skill=[]
    in_percent=[]
    interest=[]
    
    for i in data[0].language.split(','):
        language.append(i)
        
    for i in data[0].skill.split(','):
        skill.append(i)
        
    for i in data[0].in_percent.split(','):
        in_percent.append(i)
    
    for i in data[0].interest.split(','):
        interest.append(i)
        
    context={
        'data':data,
        'language':language,
        'skill':skill,
        'interest':interest,
        'in_percent':in_percent,
    }
    return render(request,'cv.html',context)

# cv_forms.html form page
def cv_forms(request):
    if request.method=="POST":
        a=cv_form(request.POST, request.FILES)
        print(a)
        if a.is_valid():
            a.save()
            return redirect('/cv/')
        
    a=cv_form()
    context={
            'a':a
    }
    return render(request,'cv_forms.html',context) 

## CREATE ACCOUNT PAGE
def Create_Account(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        passw=request.POST.get('password')
        print(uname,email,passw)
        
        if User.objects.filter(username=uname).first():
            messages.success(request,'username is taken')
            
        if User.objects.filter(email=email).first():
            messages.success(request,'email is taken')
            
        else:
            user = User(username=uname,email=email)
            user.set_password(passw)
            user.save()
            messages.success(request,'account create !!')
    
    return render(request,'create_account.html')

## LOGIN PAGE 
def login_page(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password =request.POST.get('password')
            print(username,password)
           
            if not username or not password:
                messages.success(request,'Boths fields are required !')

            user_obj = User.objects.filter(username=username).first()
            user = authenticate(username=username,password=password)

            if user_obj is None:
                messages.success(request,'User Not found !')
            print(user_obj)

            if user is not None:
                login(request,user)
                return redirect('/cv_forms/')
            
            if user is None:
                messages.success(request,'Wrong Password !!')

    return render(request,'login.html')