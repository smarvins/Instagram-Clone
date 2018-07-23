# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . models import Post, Profile
from django.test import TestCase
from django.contrib.auth.models import User

class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('','')
        self.image = Image.objects.create(image_link='posts/', name='',caption='',created_by=self.user)
    def test_instance(self):
        self.image.save()
        self.assertTrue(isinstance(self.Post,Post))
