# -*- coding: utf-8 -*-
'''站点Admin-Api'''
from flask import jsonify

from . import admin_app


@admin_app.route(r'/user/list', methods=['GET', 'POST'])
def user_list_ajax():
    ret = {}
    return jsonify(ret)

@admin_app.route(r'/user/save', methods=['POST'])
def user_save_ajax():
    ret = {}
    return jsonify(ret)

@admin_app.route(r'/user/delete-disable', methods=['GET', 'POST'])
def user_delete_or_disable():
    ret = {}
    return jsonify(ret)