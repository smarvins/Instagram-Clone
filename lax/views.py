from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm,ProfileForm,PostForm
from annoying.decorators import ajax_request
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import transaction
from django.core.urlresolvers import reverse
from .models import Profile,Post,Comment,Like


''' The homepage is your timeline page on instagram '''

@login_required(login_url='accounts/login/')
def homepage(request):
    # This will only bring users that you are Following
    users_followed = request.user.profile.following.all()
    posts = Post.objects.filter(profile_in= users_followed).order_by('-posted_on')

    return render(request,'index.html',{"posts":posts})
#####################################################################
'''This is your profile section where you'll be in control of your account'''
@login_required
def profilepage(request, username):
    user = User.objects.get(username= username)
    if not user:
        return redirect('Home')
    profile = Profile.objects.get(user= user)
    title = "{user.username}"
    return render(request, 'profiles/profile.html', {"title":title,"user":user,"profile":profile})
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
'''A section where you will be able to post images'''
@login_required
def posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST,files= request.FILES)
        if form.is_valid():
            post = Post(profile= request.user.profile, title= request.POST['image'])
            post.save()
            return redirect('profile', kwargs={'username':request.user.username})
    else:
        form = PostForm()
    return render(request, 'post_picture.html', {"form":form})
#####################################################################
'''A section where you will be able to *stalk* follow other people'''
def followers(request, username):
  user = user = User.objects.get(username = username)
  user_profile = Profile.objects.get(user=user)
  profiles = user_profile.followers.all

  title = "Followers"

  return render(request, 'follow_list.html', {"title": title, "profiles":profiles})
