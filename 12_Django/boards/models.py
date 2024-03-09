from django.db import models
from common.models import CommonModel

# 게시글
# - title
# - content
# - writer
# - date
# - like
# - reviews

class Board(CommonModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True) # 오토나우애드는 현재 시간을 기준으로 하겠다 라는 뜻
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    