# Django JWT (SimpleJWT)

## **`djangorestframework-simplejwt`** 을 활용한 JWT 인증

### **1. 준비사항**

**`djangorestframework-simplejwt` 라이브러리 설치**

```bash
> pip install djangorestframework-simplejwt # venv
> poetry add djangorestframework-simplejwt # poetry
```

### **2. 프로젝트 및 앱 설정**

**config/settings.py**

```python
INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]
```

```python

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        **'rest_framework_simplejwt.authentication.JWTAuthentication'**
    )
    ...
}
```

- **`BasicAuthentication`**은 HTTP 기본 인증을 사용합니다.
- **`SessionAuthentication`**은 장고의 세션 프레임워크를 이용한 인증을 사용합니다.
- **`TokenAuthentication`**은 토큰 기반 인증을 사용합니다.

### **3. JWT 인증 설정**

**`settings.py`**에서 Django REST framework의 기본 인증 설정을 JWT 인증으로 변경합니다.

- **설정값 예시**
    
    ```python
    from datetime import timedelta
    
    SIMPLE_JWT = {
    		# 액세스 토큰의 유효 기간을 5분으로 설정합니다.
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    	
        # 리프레시 토큰의 유효 기간을 1일로 설정합니다.
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
        
        # 리프레시 토큰을 갱신할 때마다 새 토큰을 생성하지 않도록 설정합니다.
        'ROTATE_REFRESH_TOKENS': False,  
    
        # 토큰을 갱신한 후 이전 토큰을 블랙리스트에 추가합니다.
        'BLACKLIST_AFTER_ROTATION': True,
    
        # JWT에 사용할 서명 알고리즘으로 HS256을 사용합니다.
        'ALGORITHM': 'HS256',
    
        # JWT를 서명하는 데 사용할 키로 Django의 SECRET_KEY를 사용합니다.
        'SIGNING_KEY': SECRET_KEY,
    
        # JWT 검증에 사용할 키입니다. HS256 알고리즘에서는 None으로 설정됩니다.
        'VERIFYING_KEY': None,  
    
        # 인증 헤더의 타입으로 'Bearer'를 사용합니다.
    		# Authorization: Bearer <token>
        'AUTH_HEADER_TYPES': ('Bearer',),
    
        # 토큰에 포함될 사용자 식별자 필드로 'id'를 사용합니다.
        'USER_ID_FIELD': 'id',  
    
        # 토큰 클레임에서 사용자 식별자에 해당하는 키로 'user_id'를 사용합니다.
        'USER_ID_CLAIM': 'user_id',  
    
        # 사용할 토큰 클래스로 AccessToken을 사용합니다.
        'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),  
    }
    ```
    
    - **`Bearer`**
        1. **표준 규약**: "Bearer" 용어는 OAuth 2.0 표준에서 정의되었으며, 토큰 기반 인증에서 널리 사용됩니다. 이 표준화된 접근 방식을 사용함으로써, 개발자들은 보편적으로 인정받는 방식을 따를 수 있으며, 다른 시스템과의 호환성을 유지할 수 있습니다.
        2. **명확한 의미 전달**: "Bearer"라는 단어는 토큰의 소지자가 해당 자원에 대한 액세스 권한을 가지고 있다는 것을 명확하게 전달합니다. 이는 다른 단어들보다 이 목적에 더 적합합니다.
        
        결론적으로, "Bearer"라는 용어는 토큰 기반 인증에서 널리 사용되고 인정받는 표준 용어이기 때문에 사용되고 있습니다.
        
- **자주사용하는 설정값**
    
    ```bash
    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=14),
        "SIGNING_KEY": "SECRET",
        "ALGORITHM": "HS256",
        "AUTH_HEADER_TYPES": ("Bearer",),
    }
    ```
    
    - **ACCESS_TOKEN vs REFRESH_TOKEN**
        
        **액세스 토큰 (Access Token)**
        
        - **목적**: 사용자의 인증 정보를 담고, API 접근 권한을 부여하는 짧은 기간의 토큰입니다.
        - **유효 기간**: 일반적으로 짧게 설정됩니다 (예: 5분에서 1시간).
        - **보안**: 짧은 유효 기간으로 인해, 토큰이 탈취되더라도 공격자가 오랜 시간 동안 사용할 수 없습니다.
        
        **리프레시 토큰 (Refresh Token)**
        
        - **목적**: 액세스 토큰이 만료되었을 때 새로운 액세스 토큰을 발급받기 위해 사용하는 긴 기간의 토큰입니다.
        - **유효 기간**: 일반적으로 길게 설정됩니다 (예: 7일에서 30일). 이 예제에서는 14일로 설정되어 있습니다.
        - **보안**: 비교적 긴 유효 기간을 가지지만, 오직 새로운 액세스 토큰을 발급받는 용도로만 사용됩니다.
        
        **설계 팁**
        
        **1. 유효 기간의 균형**
        
        - **액세스 토큰**: 액세스 토큰은 짧은 유효 기간(예: 5분에서 1시간)을 가짐으로써, 탈취되더라도 제한된 시간 동안만 유효합니다. 이는 토큰이 노출되었을 경우의 위험을 줄여줍니다.
        - **리프레시 토큰**: 리프레시 토큰은 긴 유효 기간(예: 7일에서 30일)을 가짐으로써, 사용자가 자주 로그인을 반복하는 불편함을 줄여줍니다. 그러나 이는 동시에 토큰이 탈취될 위험을 증가시킬 수 있습니다.
        
        **2. 액세스 토큰 만료 시 리프레시**
        
        - 사용자가 계속해서 서비스를 이용하는 동안에는, 액세스 토큰이 만료되어도 자동으로 리프레시 토큰을 사용하여 새로운 액세스 토큰을 발급받을 수 있어야 합니다. 이를 위해 클라이언트 측 애플리케이션은 액세스 토큰의 만료를 감지하고, 필요 시 리프레시 토큰을 이용해 새 토큰을 요청하는 로직을 구현해야 합니다.
        
        **3. 리프레시 토큰의 안전한 저장**
        
        - 리프레시 토큰은 상대적으로 긴 유효 기간을 가지므로, 안전한 저장소에 보관되어야 합니다. 예를 들어, 서버 측에서는 데이터베이스에 안전하게 저장하고, 클라이언트 측에서는 적절하게 암호화된 형태로 로컬 저장소에 보관해야 합니다.
        
        **4. 리프레시 토큰의 재발급 고려**
        
        - 보안을 강화하기 위해, 리프레시 토큰을 사용할 때마다 새로운 리프레시 토큰을 발급하고, 이전 토큰은 무효화하는 것이 좋습니다. 이렇게 하면, 리프레시 토큰이 탈취되더라도 탈취자가 오랫동안 사용할 수 없게 됩니다.
        
        **5. 비정상적 접근 감지**
        
        - 서버는 토큰 사용 패턴을 모니터링하여 비정상적인 접근을 감지해야 합니다. 예를 들어, 짧은 시간 내에 여러 국가에서 동일한 토큰으로 요청이 들어오는 경우, 이는 토큰이 탈취되었을 가능성이 있습니다. 이런 경우에는 즉시 해당 토큰을 무효화하고, 사용자에게 경고를 보내어 추가 조치를 취하도록 해야 합니다.
        - **ACCESS_TOKEN과 REFRESH_TOKEN을 분리하는 이유**
            
            액세스 토큰과 리프레시 토큰을 분리하여 사용하는 이유
            
            1. **보안 강화를 위한 분리**: 액세스 토큰과 리프레시 토큰을 분리함으로써, 두 토큰이 각각 다른 목적으로 사용되고, 이에 따라 다른 보안 수준을 적용할 수 있습니다. 액세스 토큰은 짧은 유효 기간을 가지므로, 실제 리소스에 접근하는 데 사용되며, 만약 탈취되더라도 짧은 시간 동안만 유효합니다. 반면, 리프레시 토큰은 오랜 기간 동안 유효하지만, 오직 새로운 액세스 토큰을 발급받는 데만 사용됩니다.
            2. **성능과 효율성 향상**: 액세스 토큰은 상대적으로 짧은 유효 기간을 가지므로, 자주 갱신해야 합니다. 이는 서버에 부하를 줄이고, 사용자의 요청 처리 속도를 빠르게 하기 위한 선택입니다. 짧은 유효 기간의 액세스 토큰을 사용함으로써, 각 요청에 대한 인증 과정을 빠르게 처리할 수 있습니다.
            3. **세션 유지의 편의성**: 리프레시 토큰은 사용자가 자주 로그인을 반복하는 것을 방지합니다. 사용자가 서비스를 지속적으로 이용하는 동안에는, 리프레시 토큰을 사용해 자동으로 새로운 액세스 토큰을 발급받을 수 있어, 끊임없는 사용자 경험을 제공할 수 있습니다.
            4. **토큰 탈취에 대한 대응**: 액세스 토큰이 탈취되더라도, 그 피해는 짧은 유효 기간으로 인해 제한적입니다. 반면, 리프레시 토큰이 탈취되면 보다 심각한 문제가 발생할 수 있으나, 이를 방지하기 위한 여러 보안 조치를 취할 수 있습니다 (예: 안전한 저장, 사용 패턴 모니터링, 재발급 및 무효화 등).
            
            결국, 액세스 토큰과 리프레시 토큰의 분리는 보안과 성능, 그리고 사용자 경험을 모두 고려한 설계 결정입니다. 리프레시 토큰의 보안에 특별한 주의를 기울이면서, 이 두 가지 유형의 토큰을 효과적으로 사용하면, 보다 안전하고 효율적인 인증 시스템 구축을 할 수 있습니다.
            
        - **어쨌든 REFRESH_TOKEN이 털리면 끝 아니냐?**
            1. **리프레시 토큰의 안전한 저장**: 리프레시 토큰은 매우 중요하므로, 클라이언트 측에서는 이를 안전하게 저장하고 관리해야 합니다. 예를 들어, 웹 애플리케이션에서는 쿠키에 저장하는 대신, 보안이 강화된 저장소를 사용해야 합니다.
            2. **리프레시 토큰의 재발급 및 무효화**: 리프레시 토큰을 사용할 때마다 새로운 리프레시 토큰을 발급하고, 이전 토큰을 무효화하는 방법을 고려해야 합니다. 이렇게 하면, 토큰이 탈취되었다 하더라도, 공격자가 오랜 시간 동안 그 토큰을 사용할 수 없게 됩니다.
            3. **리프레시 토큰의 사용 패턴 모니터링**: 서버는 리프레시 토큰의 사용 패턴을 모니터링하여 비정상적인 행동을 감지해야 합니다. 예를 들어, 짧은 시간 내에 다수의 액세스 토큰 발급 요청이 발생한다면 이는 의심스러운 행동으로 간주될 수 있습니다.
            4. **리프레시 토큰의 활성화 구역 제한**: 가능하다면, 리프레시 토큰의 사용을 특정 지역이나 IP 주소로 제한하는 것도 좋은 방법입니다. 이를 통해 무단 접근을 효과적으로 방지할 수 있습니다.
            5. **두 단계 인증 (Two-Factor Authentication, 2FA)**: 보안을 더욱 강화하기 위해, 사용자 계정에 대한 두 단계 인증을 도입할 수 있습니다. 이렇게 하면, 공격자가 리프레시 토큰을 탈취했더라도 추가적인 인증 단계가 있어 무단 접근을 방지할 수 있습니다.

### **4. URL 설정**

JWT 관련 뷰를 위한 URL을 설정합니다.

**`users/urls.py`**에 다음과 같이 추가합니다.

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
		TokenVerifyView
)

urlpatterns = [
		# simple JWT
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view())
]
```

~~URL 경로에서는 대소문자 구별 없이 인식~~ → URL에서 대소문자 구별해서 인식

### **TokenObtainPairView (`/login/simpleJWT`)**

- **사용 시점**: 사용자가 처음으로 로그인할 때 사용됩니다.
- **기능**: 사용자의 자격 증명 (사용자 이름과 비밀번호)을 받아서 검증하고, 유효하다면 액세스 토큰과 리프레시 토큰을 발급합니다.
- **프론트엔드 개발자의 역할**: 사용자가 로그인 폼을 통해 자격 증명을 제공하면, 이를 이 뷰에 전달하여 토큰 쌍을 받습니다.

### **TokenRefreshView (`/login/simpleJWT/refresh`)**

- **사용 시점**: 액세스 토큰이 만료되었을 때 사용됩니다.
- **기능**: 유효한 리프레시 토큰을 받아 새로운 액세스 토큰을 발급합니다.
- **프론트엔드 개발자의 역할**: 액세스 토큰이 만료되었음을 감지하면, 리프레시 토큰을 이 뷰에 전달하여 새로운 액세스 토큰을 받습니다.

### **TokenVerifyView (`/login/simpleJWT/verify`)**

- **사용 시점**: 토큰의 유효성을 검증할 필요가 있을 때 사용됩니다.
- **기능**: 제공된 액세스 토큰이 유효한지 검증합니다.
- **프론트엔드 개발자의 역할**: 토큰의 유효성을 확인하고 싶을 때 이 뷰를 사용할 수 있습니다.
- 위 함수들을 상속 받아 커스텀도 가능합니다.
    
    **`django-rest-framework-simplejwt`** 라이브러리는 **`TokenRefreshView`**와 **`TokenVerifyView`**를 이미 제공하므로 이들에 대한 별도의 view 함수를 작성할 필요는 없습니다. 그러나, 이러한 뷰의 작동 방식을 이해하고 사용자 정의를 하고 싶다면, 기본 뷰를 상속받아 확장할 수 있습니다.
    
    다음은 **`TokenRefreshView`**와 **`TokenVerifyView`**를 확장하는 방법을 보여주는 예시입니다:
    
    ### **TokenRefreshView 확장**
    
    ```python
    from rest_framework_simplejwt.views import TokenRefreshView
    from rest_framework.response import Response
    
    class CustomTokenRefreshView(TokenRefreshView):
        def post(self, request, *args, **kwargs):
            # 여기에서 커스텀 로직을 추가할 수 있습니다.
            # 예를 들어, 추가 로그 작성, 토큰 갱신 전/후 처리 등을 구현할 수 있습니다.
    
            # 부모 클래스의 post 메소드를 호출하여 기본 동작을 수행합니다.
            response = super().post(request, *args, **kwargs)
    
            # 추가 응답 데이터나 로직을 여기에 추가할 수 있습니다.
            # 예: response.data['custom_field'] = 'custom_value'
    
            return response
    ```
    
    ### **TokenVerifyView 확장**
    
    ```python
    from rest_framework_simplejwt.views import TokenVerifyView
    from rest_framework.response import Response
    
    class CustomTokenVerifyView(TokenVerifyView):
        def post(self, request, *args, **kwargs):
            # 여기에서 커스텀 로직을 추가할 수 있습니다.
            # 예를 들어, 토큰 검증 로그 작성, 추가 검증 로직 등을 구현할 수 있습니다.
    
            # 부모 클래스의 post 메소드를 호출하여 기본 동작을 수행합니다.
            response = super().post(request, *args, **kwargs)
    
            # 추가 응답 데이터나 로직을 여기에 추가할 수 있습니다.
            # 예: response.data['custom_message'] = 'Token is valid'
    
            return response
    ```
    
    이러한 커스텀 뷰를 사용하려면, Django의 URL 설정에서 기본 뷰 대신 이 커스텀 뷰를 사용해야 합니다:
    
    ```python
    from django.urls import path
    from .views import CustomTokenRefreshView, CustomTokenVerifyView
    
    urlpatterns = [
        # ...
        path('login/simpleJWT/refresh', CustomTokenRefreshView.as_view(), name='token_refresh'),
        path('login/simpleJWT/verify', CustomTokenVerifyView.as_view(), name='token_verify'),
    ]
    ```
    
    이 방법으로 **`django-rest-framework-simplejwt`**의 기본 동작에 추가적인 로직을 적용할 수 있습니다.
    

### **프론트엔드에서의 토큰 처리 방식**

- **액세스 토큰 만료 감지**: 프론트엔드 애플리케이션은 일반적으로 액세스 토큰의 만료를 감지하는 로직을 구현합니다. 이는 토큰의 유효기간 정보를 확인하거나, 서버로부터의 응답 상태 코드를 통해 이루어질 수 있습니다.
- **리프레시 토큰 사용**: 액세스 토큰이 만료되면, 프론트엔드는 저장된 리프레시 토큰을 사용하여 **`TokenRefreshView`**에 요청을 보내 새로운 액세스 토큰을 받습니다.
- **새로운 액세스 토큰 사용**: 새로 발급받은 액세스 토큰을 이후의 요청에 사용하여 서비스를 지속적으로 이용합니다.

즉, 프론트엔드 개발자는 액세스 토큰이 만료되었을 때, 리프레시 토큰만 서버에 보내 새 액세스 토큰을 받습니다. 서버는 리프레시 토큰을 검증하고, 유효하다면 새로운 액세스 토큰을 발급합니다.
