from django.urls import path
from .views import session_login

'''
Ссылка для сессионной авторизации
'''

urlpatterns = [
    path('session/login/', session_login, name='session_login'),
]