from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$',views.homepage,name ='home'),
    url(r'^profile/(?P<username>[-_\w.]+)/$',views.profilepage,name ='profile'),
    url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.update_profile, name='edit'),
    url(r'^profile/(?P<username>[-_\w.]+)/followers/$', views.followers, name='followers'),
    url(r'^profile/(?P<username>[-_\w.]+)/following/$', views.following, name='following'),
    url(r'^post/$', views.posts, name='post_picture'),
    url(r'^post/(?P<pk>\d+)/$', views.post, name='post'),
    url(r'^explore/$', views.explore, name='explore'),
    url(r'^like/$', views.add_like, name='like'),
    url(r'^comment/$', views.add_comment, name='comment'),
    url(r'^follow_toggle/$', views.follow_toggle, name='follow_toggle'),
    # url('^$',views.discoverpage,name ='discoverpage'),
    # url('^$',views.searchpage,name ='searchpage'),
    # url('^$',views.registerationpage,name ='registerationpage'),
]
