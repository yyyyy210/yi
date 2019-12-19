# !usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:Mckay
@file: articles.py.py
@time: 2019/12/12
"""
from flask import jsonify, request
from flask_restful import Resource
from ..models import Paper


class PaperApi(Resource):
    def get(self):
        lists = Paper.objects.all()
        return jsonify({'code': 0, 'data': lists, 'message': 'PaperApi get'})

    def post(self):
        data = request.json
        res = Paper(
            name=data['name'],
            courseId=data['courseId'],
            type=data['type'],
            timeType=data['timeType'],
            timeAll=data['timeAll'],
            text=data['text']
        ).save()
        return jsonify({'code': 0, 'data': res, 'message': 'PaperApi post ' + str(data['name'])})

    def delete(self, paper_id):
        if not paper_id:
            return jsonify({'code': 1, 'data': [], 'message': 'PaperApi del not Paper_id'})
        try:
            res = Paper.objects(id=paper_id)
            res.delete()
            return jsonify({'code': 0, 'data': [], 'message': 'PaperApi del'})
        except:
            return jsonify({'code': 1, 'data': [], 'message': 'PaperApi del sql not Paper_id'})

    def patch(self, paper_id):
        data = request.json
        res = Paper.objects.get(id=paper_id)
        if 'name' in data:
            res.name = data['name']
        if 'courseId' in data:
            res.courseId = data['courseId']
        if 'type' in data:
            res.type = data['type']
        if 'timeType' in data:
            res.timeType = data['timeType']
        if 'timeAll' in data:
            res.timeAll = data['timeAll']
        if 'text' in data:
            res.text = data['text']
        res.save()

        return jsonify({'code': 0, 'data': [], 'message': 'PaperApi patch'})
