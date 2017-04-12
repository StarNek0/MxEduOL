# coding:utf8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class Course(models.Model):
    name = models.DateTimeField(max_length=50, verbose_name='课程名')
    desc = models.DateTimeField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')  # TextField 无限大不限制长度
    degree = models.CharField(max_length=2, choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')))
    learn_name = models.IntegerField(default=0, verbose_name='学习时长-分钟数')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    Image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='课程方面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='名称')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源文件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
