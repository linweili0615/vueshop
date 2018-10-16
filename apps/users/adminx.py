#/usr/bin/env python3
#coding=utf-8

import xadmin
from xadmin import views
from .models import VerifyCode

class BaseSetting(object):
    #添加主题功能
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    #全局配置，后台管理标题页脚
    site_title = "vueshop后台"
    site_footer = "https://www.baidu.com/?tn=98010089_dg&ch=14"
    #菜单收缩
    menu_style = "accordion"

class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', 'add_time']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(VerifyCode, VerifyCodeAdmin)
