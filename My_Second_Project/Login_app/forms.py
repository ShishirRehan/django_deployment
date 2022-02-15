from django.contrib.auth.models import User
from Login_app import models
from django import forms




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ('facebook_id', 'profile_pic')
