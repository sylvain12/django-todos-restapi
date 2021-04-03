from django.db import models
from typing import Any

from django.db.models.query import QuerySet


class Todo(models.Model):

    class TodoManager(models.Manager):
        def get_queryset(self) -> QuerySet[Any]:
            return super().get_queryset().filter(completed=False)

    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    todosobjects = TodoManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.title}'
