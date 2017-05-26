# coding:utf8
from django.shortcuts import render
from django.views.generic import View

from .models import CourseOrg
from .models import CityDict


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        # 城市
        all_citys = CityDict.objects.all()
        return render(request, 'org-list.html', {})
