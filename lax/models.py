# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Profile(models.Model):
    biography = models.TextField(max_length = 50, blank= True)
    location = models.CharField(max_length= 30, blank= True)
    phone_number = models.IntegerField(blank= True, null= True)
    birth_date = models.DateField(null= True, blank= True)
