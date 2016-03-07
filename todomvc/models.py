# -*- coding: utf-8 -*-

from django.db import models


class Task(models.Model):

    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
