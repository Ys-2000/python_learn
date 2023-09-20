# /urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"

# 从 Django 3.1 开始，url 函数已经被废弃，官方建议使用 path 或 re_path 函数来定义 URL 模式
from django.urls import re_path, path, include
from . import views, testdb, search, search2
from django.contrib import admin

# urlpatterns = [
#     re_path(r'^$', views.hello),
#     # re_path('hello/', views.hello),  # 在端口号后加/hello访问
# ]


# urlpatterns = [
#     path('runoob/', views.runoob),
#     path('testdb/', testdb.testdb),
#     re_path(r'^hello/$', views.runoob),
#     re_path(r'^testdb/$', testdb.testdb),
#     re_path(r'^search-form/$', search.search_form),
#     re_path(r'^search/$', search.search),
# ]

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^hello/$', views.hello),
    re_path(r'^testdb/$', testdb.testdb),
    re_path(r'^search-form/$', search.search_form),
    re_path(r'^search/$', search.search),
    re_path(r'^search-post/$', search2.search_post),
    path('runoob/', views.runoob),
    # path('runoob/', views.test,),
    path('test/', views.base_view,),
    path('', views.hello),
    path('login/', views.login, name="login"),
    # path("app01/", include("TestModel.urls")),
]
