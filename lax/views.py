# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


''' The homepage is your timeline page on instagram '''
def homepage(request):
    return HttpResponse('This will be the homepage')
#####################################################################
'''This is your profile section where you'll be in control of your account'''
def profilepage(request):
    return HttpResponse('This shall be the profilepage')
#####################################################################
'''A section where you will be able to see other people's images the ones you don't follow'''
def discoverpage(request):
    return HttpResponse('This shall be the discoverpage')
#####################################################################
'''A section where you can search for other users based on their profile name (nickname in short)'''
def searchpage(request):
    return HttpResponse('This shall be the searchpage')
#####################################################################
'''Another section where you'll be registered to enter the website '''
def registerationpage(request):
    return HttpResponse('This shall be where you will sign in/up')
#####################################################################
