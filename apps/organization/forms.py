# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/27 22:30'
import re
from django import forms
from operation.models import UserAsk


# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=30)
#     phone = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, max_length=50)


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):  # 正则对mobile验证函数必须用clean开头
        # 验证手机号码是否合法函数
        mobile = self.cleaned_data['mobile']
        regex_mobile = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
        p = re.compile(regex_mobile)

        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法', code='mobile_invalied')
