from django.db import models


# Create your models here.

# admin pannel에 아래 데이터가 보여봤자 의미가 없음. 
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # 해당 object 생성 시간을 기준 -> 이후 데이터가 업데이트 되지 않는다.
    updated_at = models.DateTimeField(auto_now=True) # 해당 object가 업데이트된 시간을 기준 -> 이후 데이터가 수정 되면 현재시간 기준으로 업데이트 된다.

    # Meta클래스는 권한, 데이터베이스 이름, 단 복수 이름, 추상화, 순서 지정 등과 같은 모델에 대한 다양한 사항을 정의하는 데 사용
    class Meta:
        abstract = True # DB 테이블에 추가하는 것을 원하지 않는다.

# 위 설정은 CommonModel이 추상 기반 클래스임을 나타냅니다.
# 추상 기반 클래스는 데이터베이스에 직접적으로 매핑되지 않으며 테이블을 생성하지 않습니다.
# 대신, 이 클래스를 상속받은 다른 모델들이 CommonModel의 필드와 메소드를 사용할 수 있습니다.
# 이 방식은 코드 중복을 피하고, 여러 모델에 걸쳐 공통적인 필드를 일관되게 유지하는 데 유용합니다.