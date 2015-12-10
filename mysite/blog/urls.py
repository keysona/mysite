#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-12-07 22:20:13
# @Last Modified by:   key
# @Last Modified time: 2015-12-09 20:01:38
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from blog.views import index,article,tags
from django.conf.urls.static import static

STATIC_URL = '/static/'
STATIC_ROOT = '/home/key/project/mysite/static'

urlpatterns = [
    url(r'^$',index),
    url(r'^article/(.+)',article),
    url(r'^tags/(.+)',tags),
]
