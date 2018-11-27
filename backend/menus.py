from flask import render_template_string

from .apps.auth.main import AUTH_NAME

sidebar = [
    {
        'icon': 'fa fa-dashboard',
        'text': '概览',
        'type': 'url4',
        'value': 'admin.view_index'
    },
    {
        'icon': 'fa fa-file-text',
        'text': '测试',
        'type': 'group',
        'value': [
            {
                'icon': 'fa fa-circle-o',
                'text': '空白页',
                'type': 'url4',
                'value': 'admin.view_test_blank'
            },
            {
                'icon': 'fa fa-circle-o',
                'text': '玖亖伍',
                'type': 'href',
                'value': 'https://blog.gsw945.com/'
            }
        ]
    },
    {
        'icon': 'fa fa-users',
        'text': '用户系统',
        'type': 'group',
        'value': [
            {
                'icon': 'fa fa-address-card-o',
                'text': '用户管理',
                'type': 'url4',
                'value': 'admin.view_user_sys_user'
            },
            {
                'icon': 'fa fa-street-view',
                'text': '角色管理',
                'type': 'url4',
                'value': 'admin.view_user_sys_role'
            },
            {
                'icon': 'fa fa-sitemap',
                'text': '角色管理',
                'type': 'url4',
                'value': 'admin.view_user_sys_permission'
            }
        ]
    }
]