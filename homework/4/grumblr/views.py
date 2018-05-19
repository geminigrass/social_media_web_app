from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.mail import send_mail

# Create your views here.
from django.template.backends import django
from django.urls import reverse

from grumblr.forms import *

from grumblr.models import Article
import datetime


def home(request):
    return render(request,'home.html')



@login_required(login_url='/home')
def follow(request, username):
    user_to_follow = get_object_or_404(User,username=username)
    curr_user = request.user
    # context = {'post_list': ''}

    if not curr_user.username == user_to_follow.username:
        profile_to_edit = curr_user.userprofile
        profile_to_edit.follow_list.add(user_to_follow)
        post_list = Article.objects.filter(author__in=profile_to_edit.follow_list.all())
        # context['post_list'] = post_list
    return redirect(reverse('follower_stream'))

@login_required(login_url='/home')
def unfollow(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    curr_user = request.user
    # context = {'post_list': ''}

    if not curr_user == user_to_unfollow:
        profile_to_edit = curr_user.userprofile
        profile_to_edit.follow_list.remove(user_to_unfollow)
        post_list = Article.objects.filter(author__in=profile_to_edit.follow_list.all())
        # context['post_list'] = post_list
    return redirect(reverse('follower_stream'))



@login_required(login_url='/home')
def edit_profile(request):
    context = {'user_form': EditProfileForm()}

    if request.method == 'GET':
        return render(request, 'edit_profile.html', context)

    user_form = EditProfileForm(request.POST,request.FILES,instance=request.user)
    context['user_form']=user_form

    if not user_form.is_valid():
        return render(request, 'edit_profile.html', context)

    user_to_edit = request.user
    userprofile_to_edit = UserProfile.objects.get(user=user_to_edit)
    user_form.save(user_to_edit,userprofile_to_edit)

    return redirect(reverse('view_profile',
                            kwargs={'username': user_to_edit.username}))


@login_required(login_url='/home')
def change_password(request):
    context = {'form':PasswordChangeForm(user=request.user)}

    if request.method == 'GET':
        return render(request,'change_password.html',context)

    form = PasswordChangeForm(data=request.POST,user=request.user)
    context['form'] = form

    if not form.is_valid():
        return render(request, 'change_password.html', context)

    form.save()

    update_session_auth_hash(request,form.user)
    return redirect(reverse('home'))


@login_required(login_url='/home')
def view_profile(request,username):
    context = {'user': '', 'post_list': '', 'view_self':False, 'followed':False}
    self_user = get_object_or_404(User, username=request.user.username)
    has_user = get_object_or_404(User, username=username)
    # has_user = User.objects.filter(username=username)

    if has_user :
        user_to_view = get_object_or_404(User, username=username)
        # user_to_view = User.objects.get(username=username)
        post_of_the_user = Article.objects.filter(author=user_to_view)
        context['user'] = user_to_view
        context['post_list'] = post_of_the_user
        if self_user.username == user_to_view.username:
            context['view_self'] = True

        if self_user.userprofile.follow_list.all().filter(username=user_to_view.username):
            context['followed'] = True
    return render(request, 'profile.html', context)


def registration(request):
    context = {'form':SignUpForm()}

    if request.method == 'GET':
        return render(request, 'registration.html', context)

    form = SignUpForm(request.POST)
    context['form'] = form

    if not form.is_valid():
        return render(request, 'registration.html', context)

    user = form.save(commit=True)
    profile = UserProfile.objects.create(user=user)
    profile.save()

    token = default_token_generator.make_token(user)
    email_body = """
        Welcome! Please click the link below to confirm your registration in Grumblr:

        http://%s%s
        """ % (request.get_host(), reverse('confirm_registration', args=(user.username, token)))

    send_mail(subject="Confirm your registration",
              message=email_body,
              from_email="what@what.com",
              recipient_list=[user.email])

    return render(request, 'email_confirm.html', {'email':user.email})

def confirm_registration(request,username,token):
    user = get_object_or_404(User, username=username)

    if not default_token_generator.check_token(user, token):
        raise Http404

    auth_login(request, user)
    return redirect(reverse('home'))



@login_required(login_url='/home')
def add_article(request):#no user malformed
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.time = datetime.datetime.now()
            article.save()
            # post_list = Article.objects.all()
            # return redirect(reverse('global'))
            # return render(request,'global.html', context={'post_list':post_list})
            return redirect(reverse('global'))
    else:
        form = ArticleForm()
    return render(request, 'newpost.html', context={'form':form})




@login_required(login_url='/home')
def view_global(request):
    try:
        post_list = Article.objects.all()

    except Article.DoesNotExist:
        raise Http404
    return render(request, 'global.html', {'post_list': post_list,
                                             'error': False})
@login_required(login_url='/home')
def view_follower(request):

    curr_user = User.objects.get(username=request.user.username)
    follow_list = curr_user.userprofile.follow_list.all()
    post_list = Article.objects.filter(author__in=follow_list)

    return render(request, 'follower_stream.html', {'post_list': post_list})




