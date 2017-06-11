# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/9 14:55'
from django.conf.urls import url
from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MyCourseView

urlpatterns = [
    # 用户个人信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    # 用户头像修改
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),
    # 修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),
    # 修改邮箱的发送验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),
    # 完成修改邮箱的最后一步
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),
    # 用户课程
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
]
