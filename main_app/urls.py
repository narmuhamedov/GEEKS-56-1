from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import first_page, text_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_page/', first_page, name='first_page'),
    path('text_page/', text_page, name='text_page'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)