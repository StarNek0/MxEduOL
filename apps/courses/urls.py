# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/1 17:05'

from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentView, VideoPlayView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    # 课程详情
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    # 课程章节视频列表信息
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),
    # 课程评论页面
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comment"),
    # 添加评论 因为course_id已经放到POST中了，所以这里不需要了
    url(r'^add_comment/$', AddCommentView.as_view(), name="add_comment"),

    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),

]
