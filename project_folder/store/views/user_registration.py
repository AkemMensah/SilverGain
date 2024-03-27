from store.forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse

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
            user = User.objects.create_user(**form.cleaned_data)
            if user:
                return redirect('/')
            else:
                return JsonResponse('error')

