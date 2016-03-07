# -*- coding: utf-8 -*-


from django.conf.urls import patterns
from django.conf.urls import include


urlpatterns = patterns(
    '',
    ('^', include('todomvc.urls'))
)
