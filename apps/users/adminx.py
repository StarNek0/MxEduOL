# coding:utf8
import xadmin
from xadmin import views  # for basesetting
__author__ = 'zsdostar'
__date__ = '2017/4/15 19:21'


from.models import EmailVerifyRecord, Banner


#  主题设置:
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '慕学后台'  # title
    site_footer = '慕学在线网'  # 底部
    menu_style = 'accordion'  # 折叠用户表


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']  # 添加这行来修改默认显示列
    search_fields = ['code', 'email', 'send_type']  # 这一行是添加搜索框的
    list_filter = ['code', 'email', 'send_type', 'send_time']  # 超棒的功能，过滤器


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)  # for baseSetting
xadmin.site.register(views.CommAdminView, GlobalSettings)
