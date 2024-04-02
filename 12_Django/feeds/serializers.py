from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

# (1) 전체 데이터를 다 보여주는 Serialize
class FeedSerializer(ModelSerializer):
    user = FeedUserSerializer(read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Feed
        fields = "__all__"
					# 현재의 모델과 연결된 모델들까지 serialize 시키겠다는 뜻        
					# Feed - User 모델 => 현재 코드는 Feed 모델 객체를 직렬화 하고 있지만,
					# depth = 1 이라는 코드를 통해 User 객체도 직렬화하겠다는 뜻.
					# depth = 1 # objects도 serialize화 시킴
        depth = 1 # 뎁스가 0일때에는 유저가 아이디의 값만 노출되며, 뎁스가 1일때에는 유저데이터 모두 확인 가능함