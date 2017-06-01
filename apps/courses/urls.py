# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/1 17:05'

from django.conf.urls import url

from .views import CourseListView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
]
