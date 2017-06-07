# coding:utf8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from organization.models import CourseOrg, Teacher


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name='课程机构', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')  # TextField 无限大不限制长度
    teacher = models.ForeignKey(Teacher, verbose_name='课程讲师', null=True, blank=True)
    degree = models.CharField(max_length=2, choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), verbose_name='课程难度')
    learn_time = models.IntegerField(default=0, verbose_name='学习时长-分钟数')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    Image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='课程描述图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    category = models.CharField(default="void", max_length=20, verbose_name="课程类别")
    youneed_know = models.TextField(default='', max_length=300, verbose_name='课程须知')
    teacher_tell = models.TextField(default='', max_length=300, verbose_name='讲师说')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def get_zj_nums(self):
        # 获取课程的章节数量：外键用xxx_set方法
        return self.lesson_set.all().count()

    def get_learn_users(self):  # 获取该课的学生
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取章节信息
        return self.lesson_set.all()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def get_lesson_video(self):
        return self.video_set.all()

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名称')
    url = models.CharField(max_length=200, default='', verbose_name='访问地址')
    learn_time = models.IntegerField(default=0, verbose_name='学习时长-分钟数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='名称')
    download = models.FileField(upload_to='courses/resource/%Y/%m', verbose_name='资源文件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

