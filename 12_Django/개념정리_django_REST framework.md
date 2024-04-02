# Django REST framework 정리

### DRF란?

Django REST framework (DRF)는 Django 웹 프레임워크를 위한 강력한 및 유연한 도구 세트로, API 개발을 쉽고 효율적으로 만들어 줍니다.

**Django REST Framework 소개**

Django REST framework는 Django 애플리케이션에 RESTful API를 빠르고 쉽게 추가할 수 있도록 해줍니다. 주요 기능으로는 직렬화(serializer), APIView, 뷰셋, 라우터, 인증 및 권한, 페이징 등이 있습니다.


### 준비사항
Django REST framework 설치:
```python
> pip install djangorestframework # venv
> poetry add djangorestframework # poetry
```

### **프로젝트 및 앱 설정**

1. **settings.py 설정**:
**`myproject/settings.py`**에서 Django REST framework를 **`INSTALLED_APPS`**에 추가합니다.
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    ...
]
```

### **모델 및 직렬화(Serialization)**

1. **모델 생성** (**`app/models.py`**):
Django 모델을 정의합니다. 이 모델은 데이터베이스 테이블을 나타냅니다.
```python
from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
```

2. **모델 마이그레이션**:
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    
3. **직렬화 클래스 생성** (**`app/serializers.py`**):
모델 인스턴스를 JSON으로 변환하기 위해 직렬화 클래스를 생성합니다.
    
    ```python
    from rest_framework import serializers
    from .models import MyModel
    
    class MyModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = MyModel
            fields = ('id', 'title', 'description')
    ```

### **뷰(Views) 및 URL 설정**

1. **뷰 생성 (`app/views.py`)**

Django REST framework에서는 APIView 클래스 또는ViewSet 클래스를 사용하여 API 뷰를 생성할 수 있습니다. ViewSet을 사용하면 CRUD 연산을 쉽게 처리할 수 있습니다.

- APIView
    
    ```python
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from .models import MyModel
    from .serializers import MyModelSerializer
    
    class MyModels(APIView):
    		def get(self, request):
    				models = MyModel.objects.all()
    				serializer = MyModelSerializer(models, many=True)
    				return Response(serializer.data)
    ```
    
- ViewSet
    
    ```python
    from rest_framework import viewsets
    from .models import MyModel
    from .serializers import MyModelSerializer
    
    class MyModelViewSet(viewsets.ModelViewSet):
        queryset = MyModel.objects.all()
        serializer = MyModelSerializer(queryset)
    
    	  return Response.(serializer.data)
    ```
    

1. **URL 설정** (**`app/urls.py`**)

URL 경로를 설정하여 뷰와 연결합니다.

```python
from django.urls import path
from . import views

urlpatterns = [
		path('', views.MyModel.as_view())
]
```

### **인증 및 권한**

Django REST framework는 다양한 인증 및 권한 설정을 제공합니다. 인증 방식으로는 Token 인증, Session 인증, OAuth 등이 있으며, 권한 설정을 통해 API 접근 제어를 관리할 수 있습니다.

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

- **TokenAuthentication (인증 클래스)**
    
    이 방식은 사용자마다 고유한 토큰을 발급합니다. 클라이언트는 요청 시 HTTP 헤더에 이 토큰을 포함시켜 서버에 전송합니다. 서버는 이 토큰을 사용하여 사용자의 신원을 확인합니다. 이 방식은 주로 API에서 많이 사용됩니다.
    
- **IsAuthenticated (권한 클래스)**
    
    이 권한 설정은 사용자가 인증되었을 때만 API에 접근할 수 있게 합니다. 즉, 로그인된 사용자만 API를 사용할 수 있습니다. 로그인하지 않은 사용자가 API에 접근하려고 하면 권한 오류가 발생합니다.
    

즉, API 요청을 보낼 때 토큰 인증을 사용하고, 해당 API는 인증된 사용자만 접근할 수 있음을 의미합니다.

### **주의 사항 및 팁**

- **보안**: API를 공개적으로 제공하는 경우, 적절한 인증 및 권한 설정을 통해 보안을 강화해야 합니다.
- **페이지네이션**: 대규모 데이터셋을 처리할 때는 페이지네이션을 적용하여 성능을 최적화합니다.
- **버전 관리**: API가 발전하면서 변경될 수 있으므로, 버전 관리를 통해 API의 호환성을 유지합니다.
- **문서화**: Swagger나 Redoc과 같은 도구를 사용하여 API 문서를 자동으로 생성하고 관리할 수 있습니다.

