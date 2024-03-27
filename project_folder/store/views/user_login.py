from store.forms import UserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login, authenticate


def user_login(request):
    if request.method=='GET':
        form= UserLoginForm()
        return render(request,'user_login.html',{"form":form})

    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                next_path = request.session.get('next','/')
                print(request.session)
                return redirect(next_path)
            else:
                print("Invalid email or password")
        return render(request,'user_login.html',{"form":form})
        
        
