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



####################################################################################


'''This is your profile section where you'll be able to update your profile '''
@login_required
@transaction.atomic
def update_profile(request, username):
  user = User.objects.get(username = username)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance = request.user)
    profile_form = ProfileForm(request.POST, instance = request.user.profile,files =request.FILES)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, ('Your profile was successfully updated!'))
      return redirect(reverse('profile', kwargs={'username': request.user.username}))
    else:
      messages.error(request, ('Please correct the error below.'))
  else:
    user_form = UserForm(instance = request.user)
    profile_form = ProfileForm(instance = request.user.profile)
  return render(request, 'profiles/profile_form.html', {"user_form": user_form,"profile_form": profile_form})


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

 #####################################################################


 '''A section where your people will be able to 'stalk' or look at what youve been up to '''
 def following(request, username):
   user = user = User.objects.get(username = username)
   user_profile = Profile.objects.get(user=user)
   profiles = user_profile.following.all

   title = "Followinng"

   return render(request, 'follow_list.html', {"title": title, "profiles":profiles})
######################################################################


'''Here's where you like an image that has been uploaded'''
   def post(request, pk):
    post = Post.objects.get(pk=pk)
    try:
        like = Like.objects.get(post=post, user=request.user)
        liked = 1
    except:
        like = None
        liked = 0

    return render(request, 'post.html', {"post": post})


######################################################################


'''Here's where you can explore images and likes that has been posted'''
def explore(request):
  random_posts = Post.objects.all().order_by('?')[:40]
  return render(request, 'discoverpage.html', {"posts":random_posts})

def likes(request, pk):
  post = Post.objects.get(pk=pk)
  profiles = Like.objects.filter(post=post)

  title = 'Likes'
  return render(request, 'follow_list.html', {"title": title, "profiles":profiles})

