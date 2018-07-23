from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$',views.homepage,name ='home'),
    url(r'^profile/(?P<username>[-_\w.]+)/$',views.profilepage,name ='profile'),
    url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.update_profile, name='edit'),
    url('^$',views.discoverpage,name ='discoverpage'),
    url('^$',views.searchpage,name ='searchpage'),
    url('^$',views.registerationpage,name ='registerationpage'),
]
