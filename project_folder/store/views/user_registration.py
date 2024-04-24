from store.forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate,login

def user_registration(request):
    if request.method=='GET':
        form = UserRegistrationForm()
        return render(request,'user_registration.html',{'form':form})
        
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.cleaned_data.pop('phone')
            form.cleaned_data.pop('firstname')
            form.cleaned_data.pop('lastname')
            form.cleaned_data['username']=form.cleaned_data['email']
            try:
                user_account = User.objects.create_user(**form.cleaned_data)
                if not user_account:
                    return JsonResponse('error')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(request,username=email,password=password)
                if user:
                    login(request,user)
                    next_path = request.session.get('next','/')
                    return redirect(next_path)
            except Exception as Error:
                print(Error)
                context = {'error_message':'An error occured while creating your account'}
                return render(request,'product_Notfound.html',context)
               

