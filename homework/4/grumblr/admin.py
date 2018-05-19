from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

# from grumblr.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from grumblr.models import *

# admin.site.register(User, UserAdmin)
# admin.site.register(User)
admin.site.register(Article)
admin.site.register(UserProfile)
# admin.site.register(Nav_bar)
