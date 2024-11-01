from django.urls import path, include, re_path

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    re_path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
]