from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import first_page, text_page, blog_list, blog_detail
from photos.views import all_photo, picknick

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_page/', first_page, name='first_page'),
    path('text_page/', text_page, name='text_page'),
    path('blog_list/', blog_list, name='blog_list'),
    path('blog_list/<int:id>/', blog_detail, name='blog_detail'),
    path('all_photo/', all_photo, name='all_photo'),
    path('picknick/', picknick, name='picknik'),
    path('', include('todo.urls')),
    path('', include('users.urls')),
    path('captcha/', include('captcha.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)