from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.http import request


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField(default=-1,blank=True)
    bio = models.CharField(default='',blank=True,max_length=420)
    img = models.ImageField(upload_to="profile_img",null=True,blank=True)
    follow_list = models.ManyToManyField(User,symmetrical=False,
                                         related_name='follow_list',
                                         null=True, blank=True)
    def __str__(self):
        return self.user.username

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(request.FILES,user=kwargs['instance'])
#
# post_save.connect(create_profile,sender=User)

class Article(models.Model):
    title = models.CharField(max_length=42)
    author = models.ForeignKey(User)#???
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True, max_length=42)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time']
