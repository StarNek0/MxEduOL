# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/1 17:05'

from django.conf.urls import url, include

from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='org_list'),
]
