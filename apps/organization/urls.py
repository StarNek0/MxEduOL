# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/27 22:42'

from django.conf.urls import url, include
from .views import AddUserAskView

from .views import OrgView
urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask')
]
