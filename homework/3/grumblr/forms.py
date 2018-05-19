from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from requests import request

from grumblr.models import Article


class SignUpForm(forms.Form):
    username = forms.CharField(required=True, max_length=42, label='username')
    email = forms.EmailField(required=True, max_length=42, label='email')
    first_name = forms.CharField(required=True, max_length=42, label='first name')
    last_name = forms.CharField(required=True, max_length=42, label='last name')
    password = forms.CharField(required=True, max_length=42,
                               label='password', widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = ("username","email","first_name","last_name","password")['']

    # def save(self):
    #     data = self.cleaned_data
    #     user = User.objects.create_user(username=data['username'],
    #                 email=data['email'],
    #                 first_name=data['first_name'],
    #                 last_name=data['last_name'],
    #                 password=data['password'])
    #     user.save()


# class SignInForm(forms.Form):
#     username = forms.CharField(required=True, max_length=42, label='username')
#     password = forms.CharField(required=True, max_length=42,
#                                label='password', widget=forms.PasswordInput)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=42, label='title')
    # author = forms.CharField(required=True,max_length=42, label='author')  # ???
    # time = forms.DateTimeField(required=True, label='time')
    content = forms.CharField(required=True, max_length=42, label='content', widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ["title", "content"]
