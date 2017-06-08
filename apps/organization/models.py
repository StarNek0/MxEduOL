# coding:utf8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=30, verbose_name='城市名称')
    desc = models.CharField(max_length=200, verbose_name='城市描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '城市基本信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    category = models.CharField(default='pxjg', verbose_name='机构类别', max_length=20, choices=(('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')))
    click_num = models.IntegerField(default=0, verbose_name='点击量')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏量')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name='logo', max_length=100)
    address = models.CharField(max_length=200, verbose_name='机构地址')
    city = models.ForeignKey(CityDict, verbose_name='所在城市')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    course_nums = models.IntegerField(default=0, verbose_name='课程数')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '机构基本信息'
        verbose_name_plural = verbose_name

    def get_org_teacher_nums(self):
        return self.teacher_set.all().count()

    def get_org_course_nums(self):
        return self.course_set.all().count()

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    name = models.CharField(max_length=50, verbose_name='教师名称')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=50, verbose_name='就职公司名称')
    work_position = models.CharField(max_length=50, verbose_name='所在职位')
    points = models.CharField(max_length=100, verbose_name='教学特点')
    age = models.IntegerField(default=20, verbose_name='讲师年龄')
    image = models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='头像', max_length=100)
    click_num = models.IntegerField(default=0, verbose_name='点击量')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏量')
    add_time = models.DateTimeField(default=datetime.now)

    def get_teacher_course(self):
        return self.course_set.all()

    class Meta:
        verbose_name = '教师基本信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
