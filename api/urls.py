from django.urls import path
from .views import TodoDetailView, TodosListView

app_name = 'api'

urlpatterns = [
    path('todos/', TodosListView.as_view(), name='todo-list'),
    path('todo/<int:pk>', TodoDetailView.as_view(), name='todo-detail'),
]
