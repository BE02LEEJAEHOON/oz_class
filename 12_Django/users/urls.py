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
<<<<<<< HEAD
    path("login/jwt/info", views.UserDetailView.as_view()) # api 인증 테스트
]
=======
    path("login/jwt/info", views.UserDetailView.as_view()), # api 인증 테스트
    
    #Simple JWT Autentication
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view()),
]

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTUxNjExMSwiaWF0IjoxNzEwMzA2NTExLCJqdGkiOiJlMGQxMmNiNjRmNjM0MzQ4YjFhMzNlNTExOTc4N2JmNCIsInVzZXJfaWQiOjR9.XMtXtLkyLiTnz_A8it-j639MJL2LpRL_Fx1hWskVO4U",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMzEwMTExLCJpYXQiOjE3MTAzMDY1MTEsImp0aSI6ImI1MmExNTE4NjdmMTQ2ZTQ4NmNmODAzZWYzNGJiMzNmIiwidXNlcl9pZCI6NH0.2aKsBnWClhEpPM2-f4rdNA8DkKmVDpXBwo0Em9ZEMy4"
# }
>>>>>>> b99c473 (django update)
