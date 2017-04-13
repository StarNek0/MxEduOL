# coding:utf8
# 区域1：Python官方区域
from __future__ import unicode_literals
from datetime import datetime

#区域2：第三方区域
from django.db import models
from django.contrib.auth.models import AbstractUser

#区域3：自定义模块


class UserProfile(AbstractUser):  # 重载了用户profile
    nickname = models.CharField(max_length=100, verbose_name='昵称', default='', null=True, blank=True)
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=100, choices=(('male', '男'), ('female', '女')), default='female')
    address = models.CharField(max_length=100, default='', null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=(('register', '注册'), ('forget', '找回密码')))
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_type = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


