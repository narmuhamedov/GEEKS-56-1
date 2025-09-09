from django.urls import path
from . import views

urlpatterns = [
  path('todo_list/', views.read_todo_view, name='todo_list'),
  path('create_todo/', views.create_todo_view, name="create_todo"),
  path('update_todo/<int:id>/', views.update_todo_view, name='update_todo'),
  path('delete_todo/<int:id>/', views.delete_todo_view, name='delete_todo'),
]