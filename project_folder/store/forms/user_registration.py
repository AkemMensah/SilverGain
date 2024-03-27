from django import forms

class UserRegistrationForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email= forms.EmailField()
    phone = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput())
