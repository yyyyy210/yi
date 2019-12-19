# !usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:Mckay
@file: articles.py.py
@time: 2019/12/12
"""
from flask import jsonify, request
from flask_restful import Resource
from ..models import Wiki


class WikiApi(Resource):
    def get(self):
        lists = Wiki.objects.all()
        return jsonify({'code': 0, 'data': lists, 'message': 'WikiApi get'})

    def post(self):
        data = request.json
        res = Wiki(
            name=data['name'],
            CourseCategoryId=data['CourseCategoryId'],
            type=data['type'],
            tag=data['tag'],
            source=data['source'],
            text=data['text']
        ).save()
        return jsonify({'code': 0, 'data': res, 'message': 'WikiApi post ' + str(data['name'])})

    def delete(self, wiki_id):
        if not wiki_id:
            return jsonify({'code': 1, 'data': [], 'message': 'WikiApi del not Wiki_id'})
        try:
            res = Wiki.objects(id=wiki_id)
            res.delete()
            return jsonify({'code': 0, 'data': [], 'message': 'WikiApi del'})
        except:
            return jsonify({'code': 1, 'data': [], 'message': 'WikiApi del sql not Wiki_id'})

    def patch(self, wiki_id):
        data = request.json
        res = Wiki.objects.get(id=wiki_id)
        if 'name' in data:
            res.name = data['name']
        if 'CourseCategoryId' in data:
            res.CourseCategoryId = data['CourseCategoryId']
        if 'type' in data:
            res.type = data['type']
        if 'tag' in data:
            res.tag = data['tag']
        if 'source' in data:
            res.source = data['source']
        if 'text' in data:
            res.text = data['text']
        res.save()

        return jsonify({'code': 0, 'data': [], 'message': 'WikiApi patch'})