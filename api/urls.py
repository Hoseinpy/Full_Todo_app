from django.urls import path
from . import views


urlpatterns = [
    path('todo/', views.TodoListApi.as_view(), name='todo_list_api'),
    path('todo/add', views.AddTodoApi.as_view(), name='add_todo_api'),
    path('todo/<slug:slug>', views.UpdateDeleteTodoApi.as_view(), name='todo_detail_api'),
]
