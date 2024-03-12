from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication # 어떤 유저인지 식별하기 위한 api (사용자 인증?)
from rest_framework.permissions import IsAuthenticated # 특정한 api (인증된 유저들만 볼 수 있는 페이지 ?? 권한부여??)
from .serializers import MyInfoUserSerializer


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