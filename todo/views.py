from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    return render(request, 'todo/signup.html',{'form':UserCreationForm})
