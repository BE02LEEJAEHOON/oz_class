# 01. Flask란?

<img src="https://github.com/BE02LEEJAEHOON/oz_class/assets/155046462/80dbc369-8ec7-4075-9b33-d8f2f33e3c8d" width="270" height="170"/>

**특징**

- 자유도가 높다 ⇒ Django처럼 정해진 틀이 아니라 필요한 모듈들을 불러와 자유롭게 개발 가능 (→확장성이 좋다고도 표현)
- 가볍고, 간결하다 ⇒ python 파일 하나로 서버 생성 가능
- 쉽다!!!
    - 처음 파이썬으로 백엔드 서비스를 구축하는 경우 Django는 진입장벽이 있음.
        - 객체지향에 대한 이해, Django의 구조적 엄격함 등으로 인함



## **풀스택 프레임워크 vs 마이크로 프레임워크**

### **풀스택 프레임워크**

- 풀스택 프레임워크는 전체적인 애플리케이션의 개발에 필요한 모든 것을 포괄적으로 제공하는 프레임워크입니다.
- 주로 백엔드 및 프론트엔드 개발에 필요한 도구, 라이브러리, 패턴 등을 포함합니다.
- **특징:**
    - **기능의 포괄성:** 데이터베이스 처리, 서버 구축, 사용자 인터페이스 등 모든 기능을 하나의 프레임워크에서 다룹니다.
    - **내부 일관성:** 일관된 코드 구조 및 설계 원칙을 따르므로 프로젝트의 일관성을 유지하기 쉽습니다.

**대표적인 풀스택 프레임워크:**

- Java Spring, Python Django, Ruby on Rails 등

**1. Java Spring**

- **특징 및 대표적인 모듈:**
    - 스프링은 자바 기반의 오픈 소스 프레임워크로, 엔터프라이즈급 애플리케이션 개발을 위한 다양한 모듈을 제공합니다.
    - 대표적인 모듈로는 Spring MVC(웹 애플리케이션 개발), Spring Boot(마이크로서비스 개발), Spring Data(데이터 액세스), Spring Security(보안) 등이 있습니다.
- **장점:**
    - 강력한 의존성 주입(DI)과 제어 역전(IoC) 기능으로 모듈 간의 결합도를 낮추어 유지보수성을 높입니다.
    - 방대한 커뮤니티와 생태계로 빠른 문제 해결과 다양한 기능 확장이 가능합니다.
- **단점:**
    - 초기 학습 곡선이 높을 수 있습니다.

**2. Python Django**

- **특징 및 대표적인 모듈:**
    - Django는 Python 기반의 웹 프레임워크로, 고수준의 웹 개발을 위한 기능을 포괄적으로 제공합니다.
    - 대표적인 모듈로는 ORM(객체 관계 매핑), MTV(Model-Template-View) 아키텍처, Django REST framework(RESTful API 개발) 등이 있습니다.
- **장점:**
    - 기본적인 기능들이 이미 내장되어 있어 빠르게 개발을 시작할 수 있습니다.
    - 강력한 ORM 기능으로 데이터베이스 작업이 편리합니다.
- **단점:**
    - 설정이 자동으로 이루어지기 때문에 초보자에게는 이해하기 어려울 수 있습니다.

**3. Ruby on Rails**

- **특징 및 대표적인 모듈:**
    - Rails는 Ruby 언어를 기반으로 하는 웹 애플리케이션 프레임워크로, 간결한 코드와 개발자 편의성을 강조합니다.
    - 대표적인 모듈로는 MVC 아키텍처, ActiveRecord(ORM), Action Pack(웹 요청 처리) 등이 있습니다.
- **장점:**
    - 간결하고 직관적인 코드 작성이 가능하며, 개발 생산성이 높습니다.
    - 동적 언어인 Ruby의 특징을 살려 유연한 프로그래밍이 가능합니다.
- **단점:**
    - 대규모 애플리케이션에는 부적합할 수 있습니다.

### **마이크로 프레임워크**

- **개념:**
    - 마이크로 프레임워크는 작고 경량화된 프레임워크로, 필요한 부분만을 담당하고 있습니다.
    - 주로 특정 기능에 중점을 두고, 개발자가 필요한 도구 및 라이브러리를 선택적으로 추가하여 사용합니다.
- **특징:**
    - **경량성:** 필요한 부분만을 다루기 때문에 더 가벼우며, 프로젝트에 필요한 기능을 선택적으로 확장할 수 있습니다.
    - **유연성:** 다양한 도구 및 라이브러리를 조합하여 사용할 수 있어 개발자가 자유롭게 확장할 수 있습니다.
    - **학습 곡선의 낮음:** 더 적은 규모의 코드와 단순한 구조로 인해 학습이 빠르게 이루어집니다.
- 특정 기능에 초점을 맞추고 필요한 부분만을 다룹니다.
- 작은 규모와 유연성을 유지하기 위해 상대적으로 자유로운 코드 구조를 가집니다.
- 선택적으로 필요한 부분을 확장하여 사용하기 때문에 더 유연하게 확장할 수 있습니다.

**1. Flask (Python)**

- **특징:**
    - 가볍고 간단한 웹 애플리케이션을 빠르게 개발할 수 있는 마이크로 프레임워크입니다.
    - 확장성이 좋고, 필요한 기능들을 선택적으로 추가할 수 있습니다.
- **장점:**
    - 간결한 코드 작성이 가능하며, 빠른 학습 곡선
    - 확장성이 뛰어나 필요한 기능을 선택적으로 추가 가능
- **단점:**
    - 대규모 및 복잡한 애플리케이션에는 부적합

**2. Express.js (JavaScript - Node.js)**

- **특징:**
    - Node.js를 기반으로 하는 가벼운 웹 애플리케이션을 구축하기 위한 마이크로 프레임워크
- **장점:**
    - 비동기 프로그래밍에 강점, 높은 확장성.
- 단점:
    - **오버헤드의 존재**: Express 자체는 매우 가볍지만, 복잡한 애플리케이션을 구축하기 위해서는 여러 추가 모듈과 미들웨어를 선택하고 구성해야하는 단점
    - **구조적인 유연성**: Express는 구조에 대해 엄격한 규칙을 제시하지 않기 때문에, 프로젝트가 커질수록 구조적인 일관성을 유지하는 것이 어려울 수 있습니다.
 


# 02. Flask 프로젝트 세팅
  - 가상 환경 (Virtual Environment)
```python
# poetry
> poetry init
> poetry add flask

# conda
> conda create -n test_env python=3.10

# venv 가상환경 실행문
python3.10 -m venv .venv
source .venv/bin/activate
cd .\venv\Scripts\activate

# flask 실행문
> python -m flask
or
> flask run
or
> flask --app app.py --debug run
```

# 03. 라우팅(Route)

### 1. **라우팅**

- URL과 특정 함수 간의 매핑을 정의하는 것
- **`@app.route()`** 데코레이터를 사용하여 특정 URL 경로에 대한 요청이 발생했을 때 실행될 함수를 지정
- [API — Flask Documentation (2.1.x) (palletsprojects.com)](https://flask.palletsprojects.com/en/2.1.x/api/#url-route-registrations)


app.py
```python
from flask import Flask

app = Flask(__name__)
```

```python
# 기본 경로에 대한 라우트
@app.route('/')
def home():
    return 'Hello, this is the home page!'

# 다른 경로에 대한 라우트
# 127.0.0.1:5000/about
@app.route('/about')
def about():
    return 'This is the about page.'

# 127.0.0.1:5000/project
@app.route('/project')
def project():
    return 'The project page'
```

```python
# 동적인 URL 파라미터 사용
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

# URL에 변수 및 타입 지정
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'
```

```python
## API END POINT 생성 ##
# CRUD: Create(POST), Read(GET), Update(UPDATE), Delete(DELETE) -> REST API
# GET: 데이터를 요청할 때
# POST: CREATE. 데이터를 생성할 때
from flask import jsonify
@app.route("/api/v1/feeds", methods=['GET'])
def get_all_feeds():
    # DB에서 불러온다.
    data = {
        'status': 'success',
        'feed': {
            "feed1": "data",
            "feed2": "data2"
        }
    }
    # python -> dict -> json
    return jsonify(data)
```

```python
# 다양한 HTTP 메소드 지원
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        return 'POST method.'
    else:
        return 'GET method.'
```

### **`request.json` 사용하기**

JSON 형태의 데이터를 보낼 경우 (**`content-type`**이 **`application/json`**인 경우), **`request.json`** 또는 **`request.get_json()`**을 사용합니다. 이는 파이썬 딕셔너리 형태로 JSON 데이터를 자동으로 파싱해줍니다.

요청을 보내는 곳
```python
@app.route('/test')
def user_profile():
    url = 'http://localhost:5000/submit'
    data = {'key1': 'value1', 'key2': 'value2'}
    response = requests.post(url, data=data)
    return response
```

요청을 받는 곳
```python
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    key1 = data.get('key1')
    key2 = data.get('key2')
    return f'Received: key1={key1}, key2={key2}'
```

# 04. REST API 란?
<img src="https://github.com/BE02LEEJAEHOON/oz_class/assets/155046462/aaa9deeb-0595-4ea2-9ac0-d50b25d8345d" width="600" height="300"/>


REST(Representational State Transfer)란

- Representational: 표현
- State: 상태
- Transfer: 전송 (클라이언트 < == > 서버 사이의 전송)

API(Application Programming Interface)란

- 프로그램간의 상호작용을 뜻함 (데이터 교환)

RESTful한 API는 자원(Resource, 데이터) 중심으로 설계되며, HTTP 프로토콜의 메소드(GET, POST, PUT, DELETE 등)를 사용하여 해당 자원에 대한 CRUD(Create, Read, Update, Delete) 작업을 수행합니다.

- **자원 식별**: 사용자 정보 자원은 **`/users/{userId}`** URI를 통해 식별됩니다.
- **자원 표현**: 사용자 정보는 JSON, XML의 형태로 클라이언트에게 전달됩니다.
- **자원에 대한 행위**: 사용자 정보를 조회하기 위해 **`GET /users/{userId}`** 요청을 사용하고, 사용자를 생성하기 위해 **`POST /users`** 요청을 사용합니다.
    - **`GET`** (자원 읽기), **`POST`** (자원 생성), **`PUT`** (자원 업데이트), **`DELETE`** (자원 삭제).

**REST API 탄생 배경**

- 다양해진 서비스의 형태(모바일앱,웹,와치앱,티비앱)에 대응하기 위해 등장 ⇒ 안드로이드용 서버, iOS 서버, Homepage용 서버를 따로 구축하지 않아도됨.
- 이를 위해 클라이언트의 형태와 상관없이 문자열 기반의 XML, json과 같은 데이터를 주고 받게됨
- 기존에는 서비스가 대부분 웹의 형태였기 때문에 ASP, JSP, PHP 등을 사용했었음.

