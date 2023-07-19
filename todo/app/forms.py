from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import TODO
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class TODOForm(ModelForm):
    class Meta:
        model=TODO
        fields=['title','status','priority']
