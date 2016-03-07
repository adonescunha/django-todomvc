# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Task


__all__ = ['TaskSerializer']


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'completed')
