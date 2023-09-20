from django.urls import path,re_path
from TestModel import views # 从自己的 app 目录引入 views



urlpatterns = [
    path('test/', views.index),
    # re_path(r'^login/(?P<m>[0-9]{2})/$', views.index, ),
]