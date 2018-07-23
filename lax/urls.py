from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$',views.homepage,name ='home'),
    url('^profile/(?P<username>[-_\w.]+)/$',views.profilepage,name ='profile'),
    url('^$',views.discoverpage,name ='discoverpage'),
    url('^$',views.searchpage,name ='searchpage'),
    url('^$',views.registerationpage,name ='registerationpage'),
]
