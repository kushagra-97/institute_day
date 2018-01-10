from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify
# Create your models here.

class Students(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    user = models.OneToOneField(User)
   
    title = models.CharField(max_length=30,null=True)
    
    mentor = models.CharField(max_length=30,null=True)
    department = models.CharField(max_length=30,null=True)
    subarea = models.CharField(max_length=120,null=True)
    abstract = models.CharField(max_length=120,null=True)
    
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
