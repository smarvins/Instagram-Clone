from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.homepage,name ='homepage')
    url('^$',views.profilepage,name ='profilepage')
    url('^$',views.discoverpage,name ='discoverpage')
    url('^$',views.searchpage,name ='searchpage')
    url('^$',views.registerationpage,name ='registerationpage')
]
