from django.contrib import admin
from django.urls import path, include
from feeds import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("feeds/", include("feeds.urls")), # 공식 문서에서 추천하는 방식
]