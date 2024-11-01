from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import LoginJWT, LogoutJWT

urlpatterns = [
    path('login', LoginJWT.as_view(), name='LoginJWT'),
    path('logout/', LogoutJWT.as_view(), name='LogoutJWT'),
]
