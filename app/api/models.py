#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    apikey = models.CharField(max_length=30)

    def __str__(self):
        return self.user

class Host(models.Model):
    host = models.CharField(max_length=60)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.host

class Playbook(models.Model):
    playbook = models.CharField(max_length=100)

    def __str__(self):
        return self.playbook

class Log(models.Model):
    time = models.CharField(max_length=50)
    action = models.CharField(max_length=255)
    user = models.CharField(max_length=20)
    host = models.CharField(max_length=60)

    def __str__(self):
        return "%s : %s %s %s" % (self.time, self.user, self.host, self.action)
