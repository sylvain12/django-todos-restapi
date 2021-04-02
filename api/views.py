from django.shortcuts import render
from rest_framework import generics
from todos.serializer import TodoSerializer
from todos.models import Todo


class TodosListView(generics.ListCreateAPIView):
    queryset = Todo.todosobjects.all()
    serializer_class = TodoSerializer


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
