from django.conf.urls import url,include
from .views import *
from django.contrib.auth import views
from django.contrib.auth.views import *

urlpatterns=[
    url(r'^$', home),   
    url(r'^login/$', views.login, name='login'), 
    url(r'^api/v1/', include('social_django.urls', namespace='social')),
    url(r'^home/$', home, name='home'),
    url(r'^elements/$', elements, name='elements'),
    url(r'^generic/$', generic, name='generic'),
    url(r'^register/$', registration, name='registration'),
]
