from django.contrib import admin
from django.urls import path, include
from .views import home, profile, login, registration
from django.contrib.auth.views import LogoutView, PasswordChangeView



urlpatterns = [
    path('admin', admin.site.urls),

    # Ссылка для базовых функций сайта
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(next_page='profile'), name='logout'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('password_change/', PasswordChangeView.as_view(template_name='main/password_change.html', success_url='/profile/'), name='password_change'),

    # Ссылка для urls приложений
    path('api/', include('JWT_app.urls')),
    path('', include('oauth_app.urls')),
    path('', include('sessions_app.urls')),
]
