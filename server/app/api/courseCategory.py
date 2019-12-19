# !usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:Mckay
@file: articles.py.py
@time: 2019/12/12
"""
from flask import jsonify, request
from flask_restful import Resource
from ..models import CCategory


class CCategoryApi(Resource):
    def get(self):
        lists = CCategory.objects.all()
        return jsonify({'code': 0, 'data': lists, 'message': 'CCategoryApi get'})

    def post(self):
        data = request.json
        res = CCategory(
            name=data['name'],
            parentId=data['parentId'],
            text=data['text']
        ).save()
        return jsonify({'code': 0, 'data': res, 'message': 'CCategoryApi post ' + str(data['name'])})

    def delete(self, category_id):
        res = CCategory.objects(id=category_id)
        res.delete()
        return jsonify({'code': 0, 'data': [], 'message': 'CCategoryApi del'})

    def patch(self, category_id):
        data = request.json
        res = CCategory.objects.get(id=category_id)
        if 'name' in data:
            res.name = data['name']
        if 'parentId' in data:
            res.parentId = data['parentId']
        if 'text' in data:
            res.text = data['text']
        res.save()

        return jsonify({'code': 0, 'data': [], 'message': 'CCategoryApi patch'})
