from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

'''
Views для авторизации через сессию
'''

def session_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'main/login.html')
    else:
        return render(request, 'main/login.html')

