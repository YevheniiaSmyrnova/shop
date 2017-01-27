# -*- coding: utf-8 -*-
"""
Price urls module
"""
from django.conf.urls import patterns, url

from price import views

urlpatterns = patterns(
    '',
    url(r'^$', views.price, name='price')
)

