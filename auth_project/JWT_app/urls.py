from django.urls import path
from .views import LoginJWT, LogoutJWT

'''
Ссылки на авторизацию и выход из профиля для JWT.
'''

urlpatterns = [
    path('login', LoginJWT.as_view(), name='LoginJWT'),
    path('logout/', LogoutJWT.as_view(), name='LogoutJWT'),
]
