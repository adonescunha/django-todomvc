# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from django.conf.urls import include
from rest_framework import routers
from .views import TaskViewSet

router = routers.SimpleRouter()
router.register('tasks', TaskViewSet)

urlpatterns = patterns(
    '',
    (r'^', include(router.urls))
)
