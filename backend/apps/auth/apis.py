# -*- coding: utf-8 -*-
from flask import jsonify, g, request, session, url_for, abort, redirect

from . import auth_app
from .models import User, Role, Permission
from .helper import record_auth_route


LOGINED_SESSION = 'logined_user'

def login_required():
    if LOGINED_SESSION in session and 'uid' in session[LOGINED_SESSION]:
        return None
    else:
        is_ajax = request.headers.get('X-Requested-With', None) == 'XMLHttpRequest'
        is_api = 'X-Api' in request.headers
        if is_ajax or is_api:
            return abort(403)
        else:
            return redirect(url_for('admin.view_auth_login'))

@auth_app.route('/login', methods=['GET', 'POST'])
@record_auth_route('权限-登录')
def view_login():
    email = request.values.get('email')
    password = request.values.get('password')
    if bool(email) and bool(password):
        password = User.encrypt_string(password)
        Q = User.query.filter_by(email=email, password=password)
        if Q.count() > 0:
            session[LOGINED_SESSION] = Q.first().to_dict()
            ret = {
                'error': 0,
                'desc': '登录成功',
                'url': url_for('admin.view_index')
            }
        else:
            ret = {
                'error': 2,
                'desc': '用户名或密码错误'
            }
    else:
        ret = {
            'error': 1,
            'desc': '缺少参数'
        }
    return jsonify(ret)

@auth_app.route('/logout', methods=['GET', 'POST'])
@record_auth_route('注销登录', check_func=login_required)
def view_logout():
    session.pop(LOGINED_SESSION, None)
    return jsonify({
        'error': 0,
        'desc': '注销成功',
        'url': url_for('admin.view_auth_login')
    })

def ac_check():
    print('访问[{0}], 需要[{1}]权限'.format(request.endpoint, g.route_permission))
    obj = Permission.query.filter_by(name=g.route_permission).first()
    return jsonify({
        'error': 0,
        'desc': 'just a demo',
        'data': {
            'debug': '访问验证, 已阻止视图函数执行',
            'TODO': '读取用户身份信息（角色），判断权限',
            'code': {
                'permission': g.route_permission,
                'endpoint': request.endpoint
            },
            'db': obj.to_dict() if isinstance(obj, Permission) else None
        }
    })

@auth_app.route('/demo')
@record_auth_route('权限-Demo', check_func=ac_check)
def view_demo():
    return jsonify({})