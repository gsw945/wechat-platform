# -*- coding: utf-8 -*-
'''站点Admin视图'''
from flask import render_template

from .apis import admin_app
from . import app_name


@admin_app.route('/')
def view_index():
    return render_template(app_name + '/pages/index.html')

@admin_app.route('/test/blank')
def view_test_blank():
    return render_template(app_name + '/pages/test-blank.html')

@admin_app.route('/auth/login')
def view_auth_login():
    return render_template(app_name + '/pages/auth-login.html')

@admin_app.route('/auth/retrieve')
def view_auth_retrieve():
    return render_template(app_name + '/pages/auth-retrieve.html')

@admin_app.route('/user-sys/user')
def view_user_sys_user():
    return render_template(app_name + '/pages/user-sys-user.html')

@admin_app.route('/user-sys/role')
def view_user_sys_role():
    return render_template(app_name + '/pages/user-sys-role.html')

@admin_app.route('/user-sys/permission')
def view_user_sys_permission():
    return render_template(app_name + '/pages/user-sys-permission.html')