# !usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:Mckay
@file: articles.py.py
@time: 2019/12/12
"""
from flask import jsonify, request
from flask_restful import Resource
from ..models import Todo


class ArticleList(Resource):
    def get(self):
        # Todo.objects().delete()  # Removes
        # Todo(title="Simple todo A", text="12345678910").save()  # Insert
        # Todo(title="Simple todo B", text="12345678910").save()  # Insert
        Todo.objects(title__contains="Simple todo 9").update(set__text="Hello world")  # Update
        # todos = list(Todo.objects[:10])
        todos = Todo.objects.all()

        return jsonify({'code': 0, 'data': [{'name': 'one'}], 'todos': todos})
