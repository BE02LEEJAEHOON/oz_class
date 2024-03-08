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

