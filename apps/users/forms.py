# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/15 19:59'
from django import forms
from captcha.fields import CaptchaField  # 验证码


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})