"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete
from django.template.backends import django


from grumblr import views

from django.contrib.auth import views as auth_views

# from webapps import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^$',views.home,name='default'),
    url(r'^home',views.home,name='home'),
    url(r'^registration',views.registration,name='registration'),
    url(r'^login',auth_views.login,{'template_name':'login.html'},name='login'),
    url(r'^logout',auth_views.logout,{'template_name':'home.html'},name='logout'),
    url(r'^newpost',views.add_article,name='newpost'),
    url(r'^global',views.view_global,name='global'),
    url(r'^follower-stream',views.view_follower,name='follower_stream'),
    url(r'^profile/(?P<username>.+)\s',views.view_profile,name='view_profile'),
    url(r'^profile',views.view_profile,name='profile'),
    url(r'^edit-profile',views.edit_profile,name='edit_profile'),
    url(r'^password/$',views.change_password,name='change_password'),

    url(r'^reset-password/$',password_reset,
        {'template_name':'reset_password.html'},name='reset_password'),

    url(r'^reset-password/done/$',password_reset_done,
    {'template_name':'reset_password_done.html'},
        name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'template_name':'reset_password_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset-password/complete/$',password_reset_complete,
        {'template_name':'home.html'},
        name='password_reset_complete'),


    url(r'^confirm-registration/(?P<username>.+)/(?P<token>.+)$',
        views.confirm_registration,name='confirm_registration'),
    url(r'^follow/(?P<username>.+)', views.follow, name='follow'),
    url(r'^unfollow/(?P<username>.+)', views.unfollow, name='unfollow'),
    # url(r'^follow/(?P<username>.+)/$', views.follow, name='follow'),
    # url(r'^unfollow/(?P<unfollowing_id>\d+)$', views.unfollow, name='unfollow'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
