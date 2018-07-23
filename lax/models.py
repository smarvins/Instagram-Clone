# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from imagekit.models import  ProcessedImageField

class Profile(models.Model):
    user = models.ForeignKey(User)
    followers = models.ManyToManyField('Profile', related_name= 'followers_profile', blank= True)
    following = models.ManyToManyField('Profile', related_name= 'following_profile', blank= True)
    profile_pic = models.ImageField(upload_to= 'profile_pic/', null= True, blank= True)
    biography = models.TextField(max_length = 50, blank= True)
    location = models.CharField(max_length= 30, blank= True)
    phone_number = models.IntegerField(blank= True, null= True)
    birth_date = models.DateField(null= True, blank= True)

    @receiver(post_save,sender= User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender= User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def get_number_of_followers(self):
        if self.follwers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            retturn self.following.count()
        else:
            return 
    def __str__ (self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length= 70)
    profile = models.ForeignKey(Profile)
    imaage = models.ImageField(upload_to= 'posts/')
    posted_on = models.DateTimeField(auto_now_add= True)

    def get_number_of_likes(self):
        return self.like_set.count()
    def get_number_of_comments(self):
        return self.comment_set.count()

class Comment(models.Model):
    user = models.ForeignKey(Profile)
    post = models.ForeignKey(Post)
    comment = models.CharField(max_length= 70)
    post_on = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.comment

class Like(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)

    class Meta:
        unique_together =("post","user")

    def __str__(self):
        return 'Like:' + self.user.username + '' + self.post.title
