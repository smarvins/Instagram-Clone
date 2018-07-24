from django import forms
from .models import Profile,Post
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('bio', 'location','birth_date','phone_number','profile_pic')

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'image')
