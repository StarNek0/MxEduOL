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
        org_nums = all_orgs.count()
        # 城市
        all_citys = CityDict.objects.all()
        return render(request, 'org-list.html', {
            'all_orgs': all_orgs,
            'all_citys': all_citys,
            'org_nums': org_nums,
        })
