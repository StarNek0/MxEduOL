# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/1 17:05'

from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseInfoView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    # 课程详情
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),
]
