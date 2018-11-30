# -*- coding: utf-8 -*-
from datetime import datetime

import pytz
from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import BaseQuery

from .helper import classproperty
from ...utils.functions import md5


# Base = declarative_base()
from ...core.database import db
Base = db.Model

# 用户-角色-关联(['user_id', 'role_id']唯一)
user_role_map = Table('user_role_map', Base.metadata,
    Column('urid', Integer, primary_key=True, autoincrement=True, comment='主键ID'),
    Column('user_id', Integer, ForeignKey('users.uid'), nullable=False, comment='用户ID'),
    Column('role_id', Integer, ForeignKey('roles.rid'), nullable=False, comment='角色ID')
)

# 角色-权限-关联(['role_id', 'permission_id']唯一)
role_permission_map = Table('role_permission_map', Base.metadata,
    Column('urid', Integer, primary_key=True, autoincrement=True, comment='主键ID'),
    Column('role_id', Integer, ForeignKey('roles.rid'), nullable=False, comment='角色ID'),
    Column('permission_id', Integer, ForeignKey('permissions.pid'), nullable=False, comment='权限ID')
)

class User(Base):
    """用户"""
    __tablename__ = 'users'

    uid = Column('uid', Integer, primary_key=True, autoincrement=True, comment='用户ID')
    email = Column('email', String(250), unique=True, nullable=False, comment='邮箱')
    password = Column('password', String(32), nullable=False, comment='密码')
    nickname = Column('nickname', String(50), nullable=True, comment='昵称')
    register_time = Column(
        'register_time',
        DateTime(timezone=True),
        default=datetime.now(tz=pytz.timezone('Asia/Shanghai')),
        comment='注册时间'
    )
    disable = Column("disable", Boolean(create_constraint=False), default=False) # 是否禁用
    deleted = Column("deleted", Boolean(create_constraint=False), default=False) # 是否标记为删除

    roles = relationship('Role',
        secondary=user_role_map,
        backref=backref('users', lazy='dynamic'),
        lazy='dynamic'
    )

    def __init__(self, email=None, password=None, nickname=None):
        self.email = email
        self.password = password
        self.nickname = nickname

    def to_dict(self):
        return {
            'uid': self.uid,
            'email': self.email,
            'nickname': self.nickname,
            'disable': self.disable
        }

    def __repr__(self):
        return '<{0} {1!r}>'.format(__class__.__name__, self.email)

    @classmethod
    def encrypt_string(cls, raw_str, mix=''):
        '''加密算法(需要保密)'''
        ret = md5(raw_str)
        ret = md5(ret[::2]) + md5(ret[::3])
        ret = md5(ret) + md5(ret[::5])
        ret = ret[3:-3][5:] + mix
        ret = md5(ret)
        return ret

    @classmethod
    def verify_encrypt(cls, raw_str, encrypted_str, mix=''):
        '''
        验证明文和密文是否对应

        :param raw_str: 明文
        :param encrypted_str: 密文
        :param_str raw_str: str
        :param_str encrypted_str: str
        :return_type: bool
        '''
        return cls.encrypt_string(raw_str, mix=mix) == encrypted_str

class Role(Base):
    """角色"""
    __tablename__ = 'roles'
    
    rid = Column('rid', Integer, primary_key=True, autoincrement=True, comment='角色ID')
    name = Column('name', String(50), unique=True, nullable=False, comment='角色名')

    permissions = relationship('Permission',
        secondary=role_permission_map,
        backref=backref('roles', lazy='dynamic'),
        lazy='dynamic'
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<{0} {1!r}>'.format(__class__.__name__, self.name)

class Permission(Base):
    """权限"""
    __tablename__ = 'permissions'
    # (['category', 'record']唯一)(['category', 'name']暂不作唯一考虑)
    __table_args__ = ()
    
    pid = Column('pid', Integer, primary_key=True, autoincrement=True, comment='权限ID')
    name = Column('name', String(128), nullable=False, comment='权限名')
    record = Column('record', String(128), nullable=False, comment='权限记录标识')
    category = Column('category', String(50), nullable=False, comment='权限分类(取值: route,menu)')

    @classproperty
    def allowed_categories(cls):
        return {
            'route': '路由',
            'menu': '菜单'
        }

    @property
    def category_text(self):
        return self.allowed_categories[self.category]

    def __init__(self, name, record, category='route'):
        self.name = name
        self.record = record
        if category not in self.allowed_categories:
            raise ValueError('category取值只能是[{0}]之一'.format('、'.join(
                map(lambda item: repr(item), self.allowed_categories.keys())
            )))
        self.category = category

    def to_dict(self):
        return {
            'pid': self.pid,
            'name': self.name,
            'record': self.record,
            'category': self.category
        }

    def __repr__(self):
        return '<{0} [{1}]-{2!r}>'.format(__class__.__name__, self.category_text, self.name)

    @classmethod
    def get_by(cls, pid=None, record=None, category=None):
        '''
        根据参数获取权限对象，2中情形:
        1. 根据pid
        2. category和record同时提供
        '''
        Q = None
        if isinstance(pid, int):
            Q = __class__.query.filter_by(pid=pid)
        elif category in cls.allowed_categories and bool(record):
            Q = __class__.query.filter_by(
                category=category,
                record=record
            )
        if isinstance(Q, BaseQuery):
            if Q.count() > 0:
                return Q.first()