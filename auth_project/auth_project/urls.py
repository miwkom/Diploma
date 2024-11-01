from django.contrib import admin
from django.urls import path, include
from .views import home, profile, login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', home, name='home'),
    path('login', login, name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='profile'), name='logout'),
    path('profile', profile, name='profile'),
    path('api/', include('JWT_app.urls')),
    path('', include('oauth_app.urls')),
    path('', include('sessions_app.urls')),
]
