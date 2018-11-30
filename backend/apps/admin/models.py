# -*- coding: utf-8 -*-
from ...core.database import db


class WechatPlugin(db.Model):
    """微信插件"""
    __tablename__ = 'wechat_plugin'
    
    wpid = db.Column('wpid', db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.uid'), nullable=False, comment='用户ID')
    plugin_name = db.Column('plugin_name', db.String(128), nullable=False, comment='插件名称')
    plugin_code = db.Column('plugin_code', db.Text, nullable=False, default='', comment='插件代码')
    plugin_version = db.Column('version', db.Integer, nullable=False, default=1, comment='插件版本')

    def __init__(self, user_id, plugin_name, plugin_code):
        self.user_id = user_id
        self.plugin_name = plugin_name
        self.plugin_code = plugin_code

    def to_dict(self):
        return {
            'wpid': self.wpid,
            'user_id': self.user_id,
            'plugin_name': self.plugin_name,
            'plugin_code': self.plugin_code,
            'plugin_version': self.plugin_version
        }

    def __repr__(self):
        return '<{0} {1!r}>'.format(__class__.__name__, self.plugin_name)

    def save_new_version(self, user_id, plugin_name, plugin_code, auto_commit=True):
        '''保存新版本'''
        wp_query = __class__.query.filter_by(
            user_id=user_id,
            plugin_name=plugin_name
        )
        wp_new = __class__(user_id, plugin_name, plugin_code)
        if wp_query.count() > 0:
            # 如果存在旧版本，则先查询最大版本号，并添加新的版本
            wp_max_obj = wp_query.order_by(__class__.plugin_version.desc()).first()
            new_version = wp_max_obj.plugin_version + 1
            # 指定新版本
            wp_new.plugin_version = new_version
        db.session.add(wp_new)
        db.session.flush()
        wp_id = wp_new.wpid
        if auto_commit:
            db.session.commit()
        return wp_id