#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-12-07 21:38:30
# @Last Modified by:   key
# @Last Modified time: 2015-12-10 14:41:57

from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=60)
    tags = models.ManyToManyField(Tag)
    pub_datetime = models.DateTimeField(auto_now_add=True)
    modify_datetime = models.DateTimeField(auto_now=True)
    hit_count = models.PositiveIntegerField(default=0)
    content = models.TextField(blank=True)

    class Meta:
        ordering =('-pub_datetime',)

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     avatar = models.SmallIntegerField(default=0)
#     email = models.EmailField()
#     name = models.CharField(max_length=30)
#     content = models.TextField(blank=True)
#     ip = models.


