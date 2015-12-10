#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-12-07 22:20:33
# @Last Modified by:   key
# @Last Modified time: 2015-12-10 14:38:36

from django.contrib import admin
from blog.models import Article,Tag

# Register your models here.
admin.site.register(Article)
admin.site.register(Tag)
