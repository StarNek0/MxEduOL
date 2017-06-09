# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/9 14:55'
from django.conf.urls import url
from .views import UserInfoView

urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
]