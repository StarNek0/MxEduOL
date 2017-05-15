# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/15 19:59'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8)
