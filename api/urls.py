from django.urls import path
from django.views.generic.base import RedirectView
from .views import TodoDetailView, TodosListView

app_name = 'api'

urlpatterns = [
    path('', RedirectView.as_view(url='/api/todos/')),
    path('todos/', TodosListView.as_view(), name='todo-list'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]
