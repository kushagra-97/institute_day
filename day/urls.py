from django.conf.urls import url
from .views import *
from django.contrib.auth.views import *

urlpatterns=[
    url(r'^$', home),    
    url(r'^home/$', home, name='home'),
    url(r'^elements/$', elements, name='elements'),
    url(r'^generic/$', generic, name='generic'),
    url(r'^register/$', registration, name='registration'),
]
