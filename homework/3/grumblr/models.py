from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=42)
    author = models.ForeignKey(User)#???
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True, max_length=42)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time']


# items shows on the navigation bar
# class Nav_bar(models.Model):
#     name = models.CharField(max_length=42)
#
#     def __str__(self):
#         return self.name


# class MyUser(AbstractUser):
#
#     def __str__(self):
#         return self.username