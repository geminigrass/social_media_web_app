from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from requests import request

from grumblr.models import *

class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, max_length=42, label='content', widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('content',)
        # widgets = {'content': forms.CharField()}


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False, max_length=42, label='first name')
    last_name = forms.CharField(required=False, max_length=42, label='last name')

    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','age','bio','img',)
        widgets = {'img':forms.FileInput()}

    def save(self,user_instance,userprofile_instance):
        data = self.cleaned_data
        user_to_edit = User.objects.get(username=user_instance.username)

        if self.cleaned_data.get('first_name'):
        # if not data['first_name'] == '':
            user_to_edit.first_name = data['first_name']
        # if not data['last_name'] == '':
        if self.cleaned_data.get('last_name'):
            user_to_edit.last_name = data['last_name']
        if self.cleaned_data.get('age'):
            if data['age'] >= 0:
                userprofile_instance.age = data['age']
        if self.cleaned_data.get('bio'):
            userprofile_instance.bio = data['bio']
        if self.cleaned_data.get('img'):
            userprofile_instance.img = self.cleaned_data.get('img')

        user_to_edit.save()
        userprofile_instance.save()
        return user_to_edit


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=42, label='email')
    first_name = forms.CharField(required=True, max_length=42, label='first name')
    last_name = forms.CharField(required=True, max_length=42, label='last name')

    class Meta:
        model = User
        fields = ("username","email","first_name","last_name","password1","password2")

class ArticleForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=42, label='title')
    content = forms.CharField(required=True, max_length=42, label='content', widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ["title", "content"]
