from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import first_page, text_page, blog_list, blog_detail, search_view
from tags.views import all_products, drinks_products, meal_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_page/', first_page, name='first_page'),
    path('text_page/', text_page, name='text_page'),
    path('', blog_list, name='blog_list'),
    path('blog_list/<int:id>/', blog_detail, name='blog_detail'),
    path('', include('todo.urls')),
    path('', include('users.urls')),
    path('captcha/', include('captcha.urls')),
    path('search/', search_view, name='search'),
    path('all_products/', all_products, name='all_products'),
    path('drinks_products/', drinks_products, name='drinks_products'),
    path('meal_products/', meal_products, name='meal_products'),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)