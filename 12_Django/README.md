# 01. Django란? 
<img src='https://github.com/BE02LEEJAEHOON/oz_class/assets/155046462/b14b9f62-c11d-4d61-93c7-c31f0b4a7a4f' width = '450' height = '300'/>


## 장고란 무엇인가?
    - 장고(Django)는 파이썬으로 만들어진 무료 오픈소스 웹 애플리케이션 프레임워크(Web Application FrameWork)이다.
    - 쉽고 빠르게 웹사이트를 개발 할 수 있도록 돕는 구성요소로 이루어진 웹 프레임워크이다.
    - 웹 사이트를 구축할 때, 비슷한 유형의 요소들이 항상 필요하다.
      회원가입, 로그인, 로그아웃과 같이 사용자 인증을 다루는 방법이나 웹사이트의 관리자 패널, 폼, 파일 업로드와 같은 것들 말이다.
      그런데 다행이도 오래전에 어떤 웹 개발자들이 새로운 웹 사이트를 개발할 때 서로 비슷한 문제들에 직면한다는 것을 깨달았다.
      그래서 팀을 조직했고 바로 사용할 수 있는 구성요소들을 갖춘 여러 프레임워크를 만들었다. 장고도 그 중 하나이다.
      다시 만들어야하는 문제에서 해방되고 새로운 웹사이트를 개발할 때 뒤따르는 간접비용을 줄일 수 있었다.

**Python Django**

    - **특징 및 대표적인 모듈:**
        - Django는 Python 기반의 웹 프레임워크로, 고수준의 웹 개발을 위한 기능을 포괄적으로 제공.
        - 대표적인 모듈로는 ORM(객체 관계 매핑), MTV(Model-Template-View) 아키텍처, Django REST framework(RESTful API 개발) 등
    - **장점:**
        - 기본적인 기능들이 이미 내장되어 있어 빠르게 개발을 시작할 수 있다.
        - 강력한 ORM 기능으로 데이터베이스 작업이 편리함.
 
## **Flask vs Django vs  vs Lambda**

**Flask**

    - 가볍다.
    - 하나 하나의 블록을 쌓아가는 방법
    - 간단한 Rest API 가 필요한 경우
    - flask가 구리다는 건 아님. 활용 방법의 차이.
    - 간단한 땅을 파는데 굴삭기 쓸 필요 없잖아요? 삽을 쓰면 되지.

**Django**

    - 풀장착

**Lambda**

    - 서버 환경 구축이 필요 없다.
    - 비용이 저렴하다.

## poetry init
    - poetry init 명령을 실행하면, pyproject.toml 파일을 설정하는 과정이 시작된다.
      pyproject.toml 파일은 프로젝트의 메타데이터와 의존성을 관리하는 데 사용되며, Poetry를 사용하는 Python 프로젝트의 핵심 구성 파일
      
    - Package Name: 프로젝트 또는 패키지의 이름이다. 일반적으로 프로젝트의 디렉토리 이름을 기본값으로 사용된다.
    - Version: 패키지의 시작 버전이다. 일반적으로 **0.1.0**으로 시작하며, 개발 진행에 따라 버전을 업데이트한다.
    - Description: 프로젝트의 간단한 설명이다. 이 내용은 PyPI 등의 패키지 저장소에 표시됨.
    - Author Name: 패키지의 작성자 또는 유지 관리자의 이름이다. 이 정보는 선택 사항이지만, 공개 패키지의 경우 중요할 수 있다.
    - License: 프로젝트에 적용할 라이선스다. Open Source 프로젝트의 경우, 일반적으로 MIT, GPL, Apache 등의 라이선스를 사용함.
    - Python Version Compatibility: 프로젝트가 호환되는 Python 버전을 지정한다. 예를 들어, **^3.7**은 Python 3.7 이상의 버전과 호환됨을 의미.
    - Dependency Specification: 프로젝트의 의존성을 지정한다. 필요한 외부 패키지를 여기에 추가할 수 있다.
    - Development Dependency Specification: 개발 시에만 필요한 의존성을 지정한다. 예를 들어, 테스팅 라이브러리나 문서화 도구 등이 여기에 해당됨.
   
## 가상환경에서 Django 실행
    - > poetry shell # 가상환경으로 접속
      > django-admin # 가상환경의 django 실행
      > exit # 밖으로 나오기
      
      > django-admin # 전역 django 실행 => 실행안됨. 가상환경에 설치한 것이기 때문에
      
      # 라이브러리 설치하려면 아래와 같이. (pip이 아님에 주의)
      > poetry add selenium

## Django 프로젝트 생성
    - django-admin startproject config . # 현재 폴더에서 프로젝트 생성 ( . 은 현재 경로)


## django-admin 명령어

### 1. 프로젝트와 앱 관리

- **startproject**
    - 새로운 Django 프로젝트를 생성합니다.
    - 사용 예: `django-admin startproject myproject`
- **startapp**
    - 프로젝트 내에 새로운 애플리케이션을 생성합니다.
    - 사용 예: `django-admin startapp myapp`

### 2. 데이터베이스 관리

- **migrate**
    - 데이터베이스 스키마를 새로운 모델 또는 모델 변경사항에 맞게 업데이트합니다.
    - 사용 예: `django-admin migrate`
- **makemigrations**
    - 모델 변경사항에 대한 마이그레이션 파일을 생성합니다.
    - 사용 예: `django-admin makemigrations`
- **sqlmigrate**
    - 특정 마이그레이션에 대한 SQL 문을 출력합니다.
    - 사용 예: `django-admin sqlmigrate myapp 0001`
- **showmigrations**
    - 프로젝트의 마이그레이션 상태를 나열합니다.
    - 사용 예: `django-admin showmigrations`

### 3. 서버 관리

- **runserver**
    - 개발 서버를 시작합니다.
    - 사용 예: `django-admin runserver`

### 4. 데이터 관리

- **dumpdata**
    - 데이터베이스의 내용을 JSON 또는 다른 형식으로 내보냅니다.
    - 사용 예: `django-admin dumpdata myapp`
- **loaddata**
    - `dumpdata`를 통해 출력된 데이터를 데이터베이스에 로드합니다.
    - 사용 예: `django-admin loaddata myapp_data.json`

### 5. 테스트 및 디버깅

- **test**
    - Django 앱의 테스트를 실행합니다.
    - 사용 예: `django-admin test myapp`
- **shell**
    - Django 프로젝트의 컨텍스트 내에서 Python 셸을 시작합니다.
    - 사용 예: `django-admin shell`

### 6. 보안 관리

- **createsuperuser**
    - 관리자 계정을 생성합니다.
    - 사용 예: `django-admin createsuperuser`
- **changepassword**
    - 사용자의 비밀번호를 변경합니다.
    - 사용 예: `django-admin changepassword myusername`

### 7. 기타 유틸리티

- **check**
    - 프로젝트의 문제를 확인합니다.
    - 사용 예: `django-admin check`
- **collectstatic**
    - 정적 파일을 한 곳으로 모읍니다.
    - 사용 예: `django-admin collectstatic`
- **clearsessions**
    - 만료된 세션을 데이터베이스에서 삭제합니다.
    - 사용 예: `django-admin clearsessions`



## 모델 (=테이블) 의 개념
    - Django에서 모델(Model)은 웹 애플리케이션의 데이터 구조를 정의하고 데이터베이스와의 상호작용을 관리하는 중요한 부분입니다. 모델은 Django의 ORM (Object-Relational Mapping) 시스템의 핵심이며, 데이터베이스 테이블과             Python 클래스를 연결합니다. 모델을 사용함으로써 복잡한 SQL 쿼리 없이 데이터베이스를 간편하게 조작할 수 있습니다.

## 모델 필드 간략한 설명
    - 숫자
        - IntegerField
        - PositiveIntegerField
    - 문자
        - CharField
        - TextField
        - URLField
        - EmailField
    - 날짜
        - DateField
        - DateTimeField
    - 기타
        - ImageField
        - JSONField

        
| 필드 타입 | 설명 | 추가 파라미터 |
| --- | --- | --- |
| CharField | 짧은 문자열 저장 | max_length=100 |
| TextField | 긴 문자열 저장 | - |
| IntegerField | 정수 저장 | - |
| BigIntegerField | 매우 큰 정수 저장 | - |
| FloatField | 부동 소수점 숫자 저장 | - |
| DecimalField | 고정 소수점 숫자 저장 | max_digits=5, decimal_places=2 |
| BooleanField | 불리언 값 (True/False) 저장 | - |
| NullBooleanField | 불리언 값이나 Null 저장 | - |
| DateField | 날짜 저장 | auto_now=True, auto_now_add=True |
| DateTimeField | 날짜와 시간 저장 | auto_now=True, auto_now_add=True |
| TimeField | 시간 저장 | - |
| DurationField | 시간 간격 저장 | - |
| ForeignKey | 다른 모델에 대한 일대다 관계 | on_delete=models.CASCADE |
| OneToOneField | 다른 모델에 대한 일대일 관계 | on_delete=models.CASCADE |
| ManyToManyField | 다른 모델에 대한 다대다 관계 | - |
| FileField | 파일 업로드 | upload_to='path/' |
| ImageField | 이미지 파일 업로드 | upload_to='path/' |
| SlugField | URL에 사용하기 좋은 짧은 레이블 | - |
| URLField | URL 저장 | - |
| UUIDField | UUID 저장 | - |
| JSONField | JSON 형식 데이터 저장 | - |
| EmailField | 이메일 주소 저장 | - |



## 모델 내 파일 구조
    - admin.py: 관리자 페이지 관련
    - apps.py: 메인 파일
    - models.py: 모델 관련 파일
    - views.py: 화면을 그려주는 파일


## Custom UserAdmin

### **1. Custom User 모델 생성하기**

먼저, 사용자 정의 User 모델을 만들어야 합니다. **`AbstractUser`**를 상속받아 필요한 필드를 추가합니다.

**`models.py`** 예제:

```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 추가 필드 예시
    age = models.PositiveIntegerField(null=True, blank=True)
```

### **2. Custom User 모델을 프로젝트에 등록하기**

**`settings.py`** 파일에서 **`AUTH_USER_MODEL`**을 설정하여 새로운 사용자 모델을 지정합니다.

```python
AUTH_USER_MODEL = 'your_app_name.CustomUser'
```

### **3. Custom UserAdmin 클래스 만들기**

이제 **`admin.py`**에서 **`UserAdmin`** 클래스를 상속받아 커스텀 클래스를 만듭니다.

**`admin.py`** 예제:

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # 추가 필드를 관리자 페이지에 표시하기 위한 설정
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )
```

### **4. 관리자 사이트에 Custom UserAdmin 등록하기**

**`admin.py`** 파일에서 **`admin.site.register()`**를 사용하여 Custom User 모델을 등록합니다.

```python
admin.site.register(CustomUser, CustomUserAdmin)
=> or
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
```

### **5. 데이터베이스 마이그레이션**

모델 변경 사항을 데이터베이스에 반영하기 위해 마이그레이션을 실행합니다.

```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. 테스트 및 확인**

마지막으로 Django 관리자 사이트에 로그인하여 CustomUser 모델이 올바르게 표시되는지 확인합니다.



## ORM (Object-Relational Mapping) 이란?
    - 객체(Object) - 장고
    - 관계형(Relational)데이터베이스 DB - RDBMS
    - 위 2개를 Mapping(연결) 시켜주는 것
    
    ⇒DB에 있는 데이터들을 객체처럼 사용할 수 있도록 도와준다.

### 자주 사용하는 함수

Django의 QuerySet은 데이터베이스 쿼리를 생성하고 실행하는 강력한 도구입니다. 각 QuerySet 메소드의 기능을 이해하고 사용하는 것은 Django 애플리케이션 개발에서 중요한 부분입니다. 아래에서는 주요 QuerySet 메소드들에 대한 설명과 예시 코드를 제공하겠습니다.

### **1. `filter()`**

- **설명**: 조건에 맞는 객체들만 포함하는 새 QuerySet을 반환합니다.
- **예시**:
    
    ```python
    from myapp.models import MyModel
    
    # name이 'John'인 객체들 전부 필터링
    queryset = MyModel.objects.filter(name='John')
    ```
    

### **2. `exclude()`**

- **설명**: 주어진 조건을 만족하지 않는 객체들만 포함하는 새 QuerySet을 반환합니다.
- **예시**:
    
    ```python
    # age가 30 미만인 객체들만 필터링
    queryset = MyModel.objects.exclude(age__lt=30)
    ```
    

### **3. `annotate()`**

- **설명**: 집계 함수를 적용하거나 쿼리 결과에 계산된 필드를 추가합니다.
- **예시**:
    
    ```python
    from django.db.models import Count
    
    # 각 카테고리별로 포함된 객체의 수를 계산
    queryset = MyModel.objects.values('category').annotate(count=Count('id'))
    ```
    

### **4. `aggregate()`**

- **설명**: **`aggregate()`** 함수는 QuerySet에 포함된 객체들에 대해 집계 연산(합계, 평균, 최소값, 최대값 등)을 수행합니다. 이 메소드는 데이터베이스 레벨에서 집계 연산을 실행하고, 그 결과를 딕셔너리 형태로 반환합니다.
- **예시**:
    
    ```python
    from django.db.models import Avg, Count, Max, Min, Sum
    
    # 모든 객체의 age 필드에 대한 평균을 계산
    average_age = MyModel.objects.aggregate(average_age=Avg('age'))
    
    # age 필드의 최대값, 최소값, 합계, 객체 수를 계산
    aggregate_values = MyModel.objects.aggregate(
        max_age=Max('age'),
        min_age=Min('age'),
        total_age=Sum('age'),
        count=Count('id')
    )
    ```
    
    이 예시에서 **`average_age`**는 평균 나이를, **`aggregate_values`**는 나이의 최대값, 최소값, 총합, 그리고 객체의 수를 각각 계산합니다. 반환된 결과는 딕셔너리 형태로, 예를 들어 **`average_age['average_age']`** 또는 **`aggregate_values['max_age']`**와 같은 방식으로 접근할 수 있습니다.
    

### 5. `order_by()`

- **설명**: QuerySet의 결과를 특정 필드에 따라 정렬합니다.
- **예시:**

```scss
# 'created_at' 필드에 따라 오름차순으로 정렬
queryset = MyModel.objects.order_by('created_at')

# 'name' 필드에 따라 내림차순으로 정렬
queryset = MyModel.objects.order_by('-name')
```

### **6. `all()`**

- **설명**: 데이터베이스의 모든 레코드를 포함하는 QuerySet을 반환합니다.
- **예시**:
    
    ```python
    # MyModel의 모든 객체를 포함하는 QuerySet
    queryset = MyModel.objects.all() # select * from
    ```
    

### **7. `get()`**

- **설명**: 단일 객체를 반환합니다. 조건에 맞는 객체가 없거나 둘 이상인 경우 예외를 발생시킵니다.
- **예시**:
    
    ```python
    # 'id'가 1인 단일 객체를 검색
    try:
        my_object = MyModel.objects.get(id=1)
    except MyModel.DoesNotExist:
        # 객체가 존재하지 않을 때 처리
    except MyModel.MultipleObjectsReturned:
        # 여러 객체가 반환됐을 때 처리
    ```
    

### **8. `exists()`**

- **설명**: QuerySet에 하나 이상의 객체가 존재하는지 여부를 확인합니다.
- **예시**:
    
    ```python
    # 조건에 해당하는 객체가 있는지 확인
    if MyModel.objects.filter(name='John').exists():
        # 처리 로직
    ```
    

### **9. `count()`**

- **설명**: QuerySet에 포함된 객체의 수를 반환합니다.
- **예시**:
    
    ```python
    # QuerySet에 포함된 객체의 수를 계산
    count = MyModel.objects.filter(name='John').count()
    ```
    

### **10. `select_related()`와 `prefetch_related()`**

- **설명**: 관련된 객체를 효율적으로 불러오기 위한 메소드입니다. **`select_related()`**는 SQL의 JOIN을 사용하여 관련 객체를 한 번의 쿼리로 불러옵니다. **`prefetch_related()`**는 별도의 쿼리를 실행하여 관련 객체를 미리 가져옵니다.
- **예시**:
    
    두 함수의 차이는 객체들을 불러오는 방식에 차이가 있습니다.
    
    **1. `select_related()` 사용 예시**
    
    - **상황**: "블로그 글"과 "작성자"가 있으며, 각 블로그 글은 하나의 작성자와 연결되어 있습니다.
    - **모델 구조**:
        
        ```python
        class Author(models.Model):
            name = models.CharField(max_length=100)
        
        class BlogPost(models.Model):
            title = models.CharField(max_length=100)
            content = models.TextField()
            author = models.ForeignKey(Author, on_delete=models.CASCADE)
        ```
        
    - **`select_related()` 사용**:
        
        ```python
        # BlogPost와 연관된 Author 객체를 한 번의 쿼리로 불러옵니다.
        posts = BlogPost.objects.select_related('author').all()
        
        for post in posts:
            print(post.title, post.author.name)
        ```
        
        여기서 **`select_related('author')`**는 BlogPost와 Author 테이블을 JOIN하여 한 번의 쿼리로 데이터를 가져옵니다. 이는 관련된 객체가 "하나"일 때 유용합니다.
        
    
    **2. `prefetch_related()` 사용 예시**
    
    - **상황**: "강사"와 "강의"가 있으며, 각 강사는 여러 강의를 진행할 수 있습니다.
    - **모델 구조**:
        
        ```python
        class Instructor(models.Model):
            name = models.CharField(max_length=100)
        
        class Course(models.Model):
            title = models.CharField(max_length=100)
            instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
        ```
        
    - **`prefetch_related()` 사용**:
        
        ```python
        # 각 Instructor에 연결된 모든 Course 객체를 별도의 쿼리로 미리 가져옵니다.
        instructors = Instructor.objects.prefetch_related('course_set').all()
        
        for instructor in instructors:
            print(instructor.name)
            for course in instructor.course_set.all():
                print(course.title)
        ```
        
        여기서 **`prefetch_related('course_set')`**는 Instructor와 연결된 모든 Course 객체를 별도의 쿼리로 가져온 후, Python에서 이를 조합합니다. 이는 관련된 객체가 "여럿"일 때 유용합니다.
        
        이러한 방식으로 **`select_related()`**와 **`prefetch_related()`**를 사용하면 데이터베이스의 부담을 줄이면서 필요한 데이터를 효과적으로 불러올 수 있습니다.

## filter() - 필터 함수 사용법
```python
from boards.models import Board
from users.models import User

# filter
User.objects.filter(is_business=False)

# (3) __ (double under score, lookup)
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/
Board.objects.filter(likes__gt=10) # likes > 10

gt=>greater than # likes > 10 (초과)
gte=>greater than equal # likes >= 10 (이상)
lt=>less than # likes < 10 (미만)
lte=>less than equal # likes <= 10 (이하)


# title에 "제목" 이라는 단어가 들어가는 객체들을 모두 반환
Board.objects.filter(title__contains="제목")

# content에 "내용" 이라는 단어가 들어가는 객체들을 모두 반환
Board.objects.filter(content__contains="내용")

# (4) create
Board.objects.create(title="제목2", content="내용2", likes=1, user=User.objects.get(pk=1))

Board.objects.create(title="추가제목", content="추가내용", likes=3, content="두 번째 피드", user_id=1)

# (5) delete
board = Board.objects.get(pk=2)
board.delete()

Board.objects.all()
# -> 삭제 된 데이터 확인

---------------------------------------------

from django.db.models import Q

# or
# filter(Q(<condition_1>|Q(<condition_2>)
Board.objects.filter(Q(content__contains="내용") | Q(likes__gt=10))

# and
# filter(<condition_1>, <condition_2>)
Board.objects.filter(content__contains="내용", likes__gt=10) # 여러 조건 적용 가능

# not
# filter(~Q(<condition>))
User.objects.filter(~Q(is_business=False))

# count
Board.objects.filter(content__contains="내용", likes__gt=10).count()

len([1,2,3])
len(QuerySet[1,2,3])
len(user.board_set.all()) => 안먹힌다.

user.board_set.all().count()
```

