from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

'''
Функции для навигации по сайту и views регистрации.
'''

def home(request):
    return render(request, 'main/home.html')

def login(request):
    return render(request, 'main/login.html')

def profile(request):
    return render(request, 'main/profile.html')

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/registration.html', {'form': form})