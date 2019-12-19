# !usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:Mckay
@file: __init__.py
@time: 2019/12/12
"""

# from flask import Blueprint
from flask_restful import Api

api = Api()

# 文章路由
from .articles import ArticleList
#
from .courseCategory import CCategoryApi
from .course import CourseApi
from .paper import PaperApi
from .question import QuestionApi
from .user import UserApi
from .wiki import WikiApi
# from .setting import setting

api.add_resource(ArticleList, '/api/articleList')
#
api.add_resource(CCategoryApi, '/api/category', '/api/category/<category_id>')
api.add_resource(CourseApi, '/api/course', '/api/course/<course_id>')
api.add_resource(PaperApi, '/api/paper', '/api/paper/<paper_id>')
api.add_resource(QuestionApi, '/api/question', '/api/question/<question_id>')
api.add_resource(UserApi, '/api/user', '/api/user/<user_id>')
api.add_resource(WikiApi, '/api/wiki', '/api/wiki/<wiki_id>')
