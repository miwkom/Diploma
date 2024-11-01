from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import RefreshToken


@method_decorator(csrf_exempt, name='dispatch')
class LoginJWT(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            response_data = {
                'access': access,
                'refresh': str(refresh)
            }
            response = Response(response_data)
            response = redirect('profile')
            response.set_cookie(
                key='jwt_token',
                value=access,
                httponly=True,
                secure=True,
                samesite='Strict',
            )
            return response
        else:
            return redirect('login')

@method_decorator(csrf_exempt, name='dispatch')
class LogoutJWT(APIView):
    def post(self, request):
        logout(request)
        response = redirect('home')
        response.delete_cookie('jwt_token')
        return response
