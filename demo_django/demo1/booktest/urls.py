from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from booktest import views
urlpatterns = [
    # path(r'books/$', views.BooksAPIVIew.as_view() ),
    # path(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view)
]
router = DefaultRouter()  # 可以处理视图的路由器
router.register(r'books', views.BookInfoViewSet)  # 向路由器中注册视图集

urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中