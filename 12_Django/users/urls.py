from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
		TokenVerifyView
)
urlpatterns = [
    path('', views.Users.as_view()), # api/v1/users/
    path('myinfo', views.MyInfo.as_view()), # api/v1/users/myinfo/
    
    # Authentication
    path('getToken', obtain_auth_token), # DRF token
    path('login', views.Login.as_view()), # Django Session login
    path('logout', views.Logout.as_view()), # Django Session logout
    
    # JWT Authentication
    path('login/jwt', views.JWTLogin.as_view()), # jwt login
    path("login/jwt/info", views.UserDetailView.as_view()) # api 인증 테스트
]
