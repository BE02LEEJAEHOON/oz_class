# Django 정리

Django의 기본적인 개념과 웹 애플리케이션을 만드는 단계 정리

### **1단계: Django 설치**

먼저 Django를 설치합니다. Django의 버전 컨트롤을 위해 가상 환경을 사용하는 것이 좋습니다.

**venv** or **poetry** 

```python
# 가상 환경 생성 (venv)
python -m venv .venv
source .venv/bin/activate # Unix, macOS에서
.venv\Scripts\activate     # Windows에서

# Django 설치
pip install django
```

```python
# 가상 환경 생성 (poetry)
poetry init
poetry shell

# Django 설치
poetry add django
```

### **2단계: 프로젝트 생성**

Django 프로젝트를 생성합니다.

```bash
django-admin startproject myproject
cd myproject
```

```python
# 현재 폴더 내에 django 프로젝트를 만들 경우
django-admin startproject config .
```

### **3단계: 앱 생성**

Django 프로젝트 내에 앱을 생성합니다.

```bash
python manage.py startapp myapp
```

### **4단계: 모델 정의**

**`myapp/models.py`** 파일에서 모델을 정의합니다. 예를 들어, 간단한 **`Post`** 모델을 만들어보겠습니다.

```python
# myapp/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

### **5단계: 모델 마이그레이션**

모델 변경사항을 마이그레이션 파일로 생성하고 데이터베이스에 적용합니다.

```bash
python manage.py makemigrations
python manage.py migrate
```

### **6단계: 관리자 페이지 설정**

**`Post`** 모델을 관리자 페이지에서 관리할 수 있도록 합니다.

```python
# myapp/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

```python
# myapp/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
		pass
```

### **7단계: View 작성**

**`myapp/views.py`**에 간단한 View 함수를 작성합니다.

```python
# myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

### **8단계: URL 설정**

**`myapp/urls.py`**를 생성하고 URL 패턴을 정의합니다.

```python
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

그리고 메인 **`urls.py`**에 **`myapp`**의 URL을 포함시킵니다.

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

### **9단계: 서버 실행 및 확인**

superuser 를 생성합니다.

```python
python manage.py createsuperuser
```

개발 서버를 실행하고 결과를 확인합니다.

```bash
python manage.py runserver
```

브라우저에서 **`http://localhost:8000/`**으로 이동하여 확인합니다.

**`http://localhost:8000/admin` →** superuser 계정 로그인

### **10단계: Jinja 템플릿 사용**

**`myapp/templates/myapp/home.html`** 템플릿 파일을 만듭니다.

```html
<!-- myapp/templates/myapp/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Hello, Django!</h1>
</body>
</html>
```

**`views.py`**를 수정하여 템플릿을 사용합니다.

```python
# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')
```
