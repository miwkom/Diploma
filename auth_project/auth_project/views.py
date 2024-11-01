from django.shortcuts import render
from requests import session


def home(request):
    return render(request, 'main/home.html')

def login(request):
    return render(request, 'main/login.html')


def profile(request):
    return render(request, 'main/profile.html')
