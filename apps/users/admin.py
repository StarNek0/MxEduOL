# coding:utf8
from django.contrib import admin

# Register your models here.注册admin


from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
