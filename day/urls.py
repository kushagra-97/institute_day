from django.conf.urls import url,include
from .views import *
from django.contrib.auth import views
from django.contrib.auth.views import *

urlpatterns=[
    url(r'^$', home),   
    url(r'^curruser/$', curruser),
    url(r'^login/$', views.login, name='login'), 
    url(r'^home/$', home, name='home'),
    url(r'^elements/$', elements, name='elements'),
    url(r'^generic/$', generic, name='generic'),
    url(r'^register/$', registration, name='registration'),
    url(r'^accounts/profile/$', registration, name='registration'),
]
