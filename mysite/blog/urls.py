#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-12-07 22:20:13
# @Last Modified by:   key
# @Last Modified time: 2015-12-11 21:37:43
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
from django.contrib import admin
from blog.views import get_args
from django.conf.urls.static import static
from blog.models import Article,Tag

home = {
    'template_name':'home.html',
}

article = {
    'template_name':'article.html',
}

tag = {
    'template_name':'home.html',
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',get_args,home),
    url(r'^article/$',get_args,home),
    url(r'^article/(?P<title>.+)/',get_args,article),
    # url(r'^tags/$',),
    url(r'^tags/(?P<tag>.+)/',get_args,tag),
]
