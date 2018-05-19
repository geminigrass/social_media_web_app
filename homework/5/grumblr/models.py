from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

# Create your models here.

from django.contrib.auth.models import User
# from grumblr.models import *
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
    last_modified = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, null=True, max_length=42)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['time']
    @staticmethod
    def get_changes(timestamp=0):
        t = datetime.datetime.fromtimestamp(timestamp/1000.0)
        return Article.objects.filter(last_modified__gt=t).distinct()

    @staticmethod
    def get_changes_follower(username,timestamp=0):
        t = datetime.datetime.fromtimestamp(timestamp / 1000.0)
        curr_user = User.objects.get(username=username)
        follow_list = curr_user.userprofile.follow_list.all()
        # return follow_list
        post_list = Article.objects.filter(author__in=follow_list,last_modified__gt=t).distinct()
        return post_list




class Comment(models.Model):
    author = models.ForeignKey(User)  # ???
    time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    content = models.CharField(blank=True, null=True, max_length=42)
    belong_to_post = models.ForeignKey(Article)

    class Meta:
        ordering = ['time']
    def __str__(self):
        return self.content

    @staticmethod
    def get_changes(timestamp=0):
        t = datetime.datetime.fromtimestamp(timestamp/1000.0)
        return Comment.objects.filter(last_modified__gt=t).distinct()

    @staticmethod
    def get_changes_follower(post_list,timestamp=0):
        t = datetime.datetime.fromtimestamp(timestamp / 1000.0)
        comment_list = Comment.objects.filter(belong_to_post__in=post_list,last_modified__gt=t).distinct()
        return comment_list


