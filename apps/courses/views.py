# coding: utf-8
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse

from .models import Course, CourseResource
from operation.models import UserFavourite, CourseComments, UserCourse
from utils.mixin_utils import LoginRequiredMixin  # 登录验证

class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by('-add_time')  # 这里的orderby直接按添加时间倒序排序

        # 右栏的推荐课程
        hot_courses = Course.objects.all().order_by('-click_nums')[:3]

        # 排序筛选功能
        sort = request.GET.get('order', "")  # HTML中的在URL中声明的变量是提交到这里进行判断的
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by('-students')
            elif sort == "hot":
                all_courses = all_courses.order_by('-click_nums')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 3, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {
            'all_courses': courses,
            'sort': sort,
            'hot_courses': hot_courses,
        })


class CourseDetailView(View):
    # 课程详情页
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        course.click_nums += 1
        course.save()

        course_hour = course.learn_time/60

        # 是否收藏课程
        has_fav_course = False
        # 是否收藏机构
        has_fav_org = False

        # 以下为课程详情页面的两个收藏功能
        if request.user.is_authenticated():
            if UserFavourite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True

            if UserFavourite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        # 以下为相似课程推荐
        type = course.category
        if type:
            near_type_courses = Course.objects.filter(category=type)[:3]
        else:
            near_type_courses = []  # 这里不能传字符串，必须是迭代器，不然出错

        return render(request, 'course-detail.html', {
            'course': course,
            'course_hour': course_hour,
            'near_type_courses': near_type_courses,
            'has_fav_org': has_fav_org,
            'has_fav_course': has_fav_course,
        })


class CourseInfoView(LoginRequiredMixin, View):  # 这里的继承顺序很重要
    # 课程章节信息
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 查询是否学习了该课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

        # 相似课程筛选
        user_courses = UserCourse.objects.filter(course=course)  # 从课程里取出所有属于这门课的行信息
        user_ids = [user_course.user.id for user_course in user_courses]  # 把这门课的用户id取出来
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)  # 以这个id为条件筛选所有的课程
        course_ids = [user_couser.course.id for user_couser in all_user_courses]  # 取出这些课程id
        # and finally
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]  # 获取学过该用户学过其他的所有课程并排序显示

        all_resources = CourseResource.objects.filter(course=course)
        return render(request, 'course-video.html', {
            'course': course,
            'course_resources': all_resources,
            'relate_courses': relate_courses,
        })


class CommentsView(LoginRequiredMixin, View):  # 这里的继承顺序很重要
    # 课程评论页面
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.filter(course=course.id).order_by('-add_time')
        return render(request, 'course-comment.html', {
            'course': course,
            'course_resources': all_resources,
            'all_comments': all_comments,
        })


class AddCommentView(View):
    # 提交评论
    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type="application/json")

        course_id = request.POST.get('course_id', 0)
        comment = request.POST.get('comments', '')  # 这里要和js代码一样的

        if course_id >0 and comment:
            course = Course.objects.get(id=int(course_id))

            course_comments = CourseComments()
            course_comments.user = request.user
            course_comments.course = course
            course_comments.comments = comment
            course_comments.save()
            return HttpResponse('{"status":"success", "msg":"评论成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"评论失败"}', content_type='application/json')
