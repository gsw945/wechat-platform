# -*- coding: utf-8 -*-
'''站点Admin视图'''
from flask import render_template

from .apis import admin_app
from . import app_name
from ..auth.apis import record_auth_route, login_required


@admin_app.route('/')
@record_auth_route(app_name + '-概览', check_func=login_required)
def view_index():
    return render_template(app_name + '/pages/index.html')

@admin_app.route('/test/blank')
@record_auth_route(app_name + '-测试-空白页', check_func=login_required)
def view_test_blank():
    return render_template(app_name + '/pages/test-blank.html')

@admin_app.route('/auth/login')
def view_auth_login():
    return render_template(app_name + '/pages/auth-login.html')

@admin_app.route('/auth/retrieve')
def view_auth_retrieve():
    return render_template(app_name + '/pages/auth-retrieve.html')

@admin_app.route('/user-sys/user')
@record_auth_route(app_name + '-用户管理-用户列表', check_func=login_required)
def view_user_sys_user():
    return render_template(app_name + '/pages/user-sys-user.html')

@admin_app.route('/user-sys/role')
@record_auth_route(app_name + '-用户管理-角色列表', check_func=login_required)
def view_user_sys_role():
    return render_template(app_name + '/pages/user-sys-role.html')

@admin_app.route('/user-sys/permission')
@record_auth_route(app_name + '-用户管理-权限分配', check_func=login_required)
def view_user_sys_permission():
    return render_template(app_name + '/pages/user-sys-permission.html')


@admin_app.route('/plugin-sys/list')
@record_auth_route(app_name + '-插件管理-插件列表', check_func=login_required)
def view_plugin_list():
    return render_template(app_name + '/pages/plugin-sys-list.html')

@admin_app.route('/plugin-sys/my')
@record_auth_route(app_name + '-插件管理-我的', check_func=login_required)
def view_plugin_my():
    return render_template(app_name + '/pages/plugin-sys-my.html')