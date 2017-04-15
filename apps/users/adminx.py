# coding:utf8
__author__ = 'zsdostar'
__date__ = '2017/4/15 19:21'

import xadmin

from.models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']  # 添加这行来修改默认显示列
    search_fields = ['code', 'email', 'send_type']  # 这一行是添加搜索框的
    list_filter = ['code', 'email', 'send_type', 'send_time']  # 超棒的功能，过滤器


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
