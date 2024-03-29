from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication # 어떤 유저인지 식별하기 위한 api (사용자 인증?)
from rest_framework.permissions import  IsAuthenticated # 특정한 api (인증된 유저들만 볼 수 있는 페이지 ?? 권한부여??)
from rest_framework import status
from .serializers import MyInfoUserSerializer
from django.contrib.auth import authenticate, login, logout



# api/v1/users [POST] -> 유저 생성 api
class Users(APIView):
    def post(self, request):
        # password => 검증을 해야하고, 해시화해서 저장 필요
        # the other => 비밀번호 외 다른 데이터들을 의미
        
        password = request.data.get("password")
        serializer = MyInfoUserSerializer(data=request.data)
        
        try:
            validate_password(password) # 비밀번호 validation
        except:
            raise ParseError("Invalid password") # 오류가 났을 때 유저에게 공유

        if serializer.is_valid():
            user = serializer.save() # 새로운 유저 생성
            user.set_password(password) # 비밀번호 업데이트(해시화)
            user.save() # 데이터 업데이트 후 저장

            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            raise ParseError(serializer.errors)
        

# api/v1/users/myinfo [GET, PUT]
class MyInfo(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, 
                                          data=request.data,
                                          partial=True) # 파셜 트루는 일부 데이터만 넘겨도 변경을 허용하겠다 라는 의미.)
        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

# api/v1/users/login (로그인은 POST 방식으로 진행해야함. GET으로 할 경우 보안에 취약함)
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            raise ParseError()
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        

# api/v1/users/logout
class Logout(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        print('header : ', request.headers)
        logout(request)
        
        return Response(status=status.HTTP_200_OK)
    
# api/v1/users/login/jwt
import jwt
from django.conf import settings

class JWTLogin(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError

        user = authenticate(request, username=username, password=password) # authenticate = 인증

        if user:
            payload = {"id": user.id, "username": user.username}
            
            token = jwt.encode(
                payload,
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            
            return Response({"token": token})


# api/v1/users/login/jwt/info
from config.authentication import JWTAuthentication        
class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username
        })