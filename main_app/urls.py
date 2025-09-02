from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import first_page, text_page, blog_list, blog_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_page/', first_page, name='first_page'),
    path('text_page/', text_page, name='text_page'),
    path('blog_list/', blog_list, name='blog_list'),
    path('blog_list/<int:id>/', blog_detail, name='blog_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)