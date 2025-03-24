from django.contrib import admin
from django.urls import path,include
from blog.views import post_list  # 直接导入

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='post_list'),  # 根路径显示文章列表
    path('', include('blog.urls')),  # 保留其他路由
]
