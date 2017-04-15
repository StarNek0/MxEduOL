# coding:utf8
__author__ = 'zsdostar'
__date__ = '2017/4/15 19:21'

import xadmin

from.models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    pass


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
