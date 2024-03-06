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
