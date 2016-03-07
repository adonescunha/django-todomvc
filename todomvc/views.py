# -*- coding: utf-8 -*-

from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task


__all__ = ['TaskViewSet']


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
