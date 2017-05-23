# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/21 19:52'
import string
from random import Random
from django.core.mail import send_mail  # Django内置邮件发送函数

from users.models import EmailVerifyRecord
from MxEduOL import settings


def random_str(randomlength=8):  # 生成随机校验码
    str = ''
    chars = string.ascii_letters + '0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):  # 发送验证邮件
    email_record = EmailVerifyRecord()  # 实例化email表
    code = random_str(16)  # 16位校验码
    email_record.code = code  # 传入数据库
    email_record.email = email
    email_record.send_type = send_type  # 类型为注册
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '慕学在线网注册激活链接'
        email_body = '请点击下边的链接激活您的账号: http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '慕学在线网账户密码重置链接'
        email_body = '请点击下边的链接重置您的密码: http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
        if send_status:
            pass
