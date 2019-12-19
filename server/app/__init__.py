# !usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:Mckay
@file: __init__.py
@time: 2019/12/12
"""

from flask import Flask
# from flask_mongoengine import MongoEngine
from flask_cors import *  # 导入模块


def create_app(config_name=None):
    # __name__ 决定应用根目录
    app = Flask(__name__)
    CORS(app, supports_credentials=True)  # 设置跨域
    app.config['MONGODB_SETTINGS'] = {
        "db": "mecbox",
        # 'host': '192.168.1.35',
        # 'port': 12345,
        # 'username': 'webapp',
        # 'password': 'pwd123',
        # 'host': 'mongodb://localhost/database_name'
    }

    # db = MongoEngine(app)
    from .models import db
    db.init_app(app)

    # 初始化api
    from .api import api
    api.init_app(app)
    # from .api import auth_api as authapi_blueprint
    # app.register_blueprint(authapi_blueprint)

    return app
