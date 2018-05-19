from datetime import timezone

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

from grumblr.forms import SignUpForm, ArticleForm, ArticleForm

from grumblr.models import Article
import datetime


def home(request):
    return render(request,'home.html')

@login_required(login_url='/home')
def view_profile(request,username):
    # context = {'user': '', 'post_list': '', 'errors': ''}
    has_user = User.objects.filter(username=username)
    print(request)


    if has_user :
        user_to_view = User.objects.get(username=username)
        print("user_to_view",user_to_view)
        post_of_the_user = Article.objects.filter(author=user_to_view)
        return render(request, 'profile.html', {'user': user_to_view,
                                                'post_list': post_of_the_user,
                                                'errors': ''})
    else:
        context = {'user': '', 'post_list': '', 'errors': ''}
        context['errors']="This user does not exist"
        return render(request, 'profile.html', context)


def registration(request):
    context = {'form':'','errors':''}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if len(User.objects.filter(username=request.POST['username'])) == 0:
                data = form.cleaned_data
                user = User.objects.create_user(username=data['username'],
                                                email=data['email'],
                                                first_name=data['first_name'],
                                                last_name=data['last_name'],
                                                password=data['password'])
                user.save()
                auth_login(request, user)
                return render(request, 'home.html', context={'user': user})
            else:#dup username in DB
                form = SignUpForm()
                context['form'] = form
                context['errors'] = "This username has been taken"
    else:
        form = SignUpForm()
        context['form'] = form
    return render(request,'registration.html',context)


@login_required(login_url='/home')
def add_article(request):#no user malformed
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.time = datetime.datetime.now()
            article.save()
            post_list = Article.objects.all()
            return render(request,'global.html', context={'post_list':post_list})
    else:
        form = ArticleForm()
    return render(request, 'newpost.html', context={'form':form})



@login_required(login_url='/home')
def view_global(request):
    try:
        post_list = Article.objects.all()
        print(post_list)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'global.html', {'post_list': post_list,
                                             'error': False})




