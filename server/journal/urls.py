from django.conf.urls import include, url
from rest_framework import routers
from journal import views

# 定义路由地址
route = routers.DefaultRouter()

# 注册新的路由地址
route.register(r'records', views.RecordViewSet)
route.register(r'category', views.CategoryViewSet)


# 注册上级路由地址
urlpatterns = [
    url('journal/', include(route.urls)),
]
