# !usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:Mckay
@file: articles.py.py
@time: 2019/12/12
"""
from flask import jsonify, request
from flask_restful import Resource, reqparse
import json
from ..models import Course


# parser = reqparse.RequestParser()

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


class CourseApi(Resource):
    def get(self):
        # "_id": {"$oid": "5df878a824fa3d5f18289725"},
        lists = Course.objects.all()
        # lists = Course.objects(id='5df885a259225f5917aeb363')
        # OrderWarningInfo.objects.filter(__raw__={'_id': ObjectId("%s" % event_id)}).update(is_finish="2")
        return jsonify({'code': 0, 'data': lists, 'message': 'CourseApi get'})

    def post(self):
        # args = parser.parse_args()
        # name = args.get('name')
        data = request.json
        res = Course(
            name=data['name'],
            CourseCategoryId=data['CourseCategoryId'],
            img=data['img'],
            timeArea=data['timeArea'],
            isBuy=data['isBuy'],
            score=data['score'],
            state=data['state'],
            text=data['text']
        ).save()
        return jsonify({'code': 0, 'data': res, 'message': 'CourseApi post ' + str(data['name'])})

    def delete(self, course_id):
        res = Course.objects(id=course_id)
        res.delete()
        return jsonify({'code': 0, 'data': [], 'message': 'CourseApi del'})

    def patch(self, course_id):
        data = request.json
        res = Course.objects.get(id=course_id)
        if 'name' in data:
            res.name = data['name']
        if 'CourseCategoryId' in data:
            res.CourseCategoryId = data['CourseCategoryId']
        if 'img' in data:
            res.img = data['img']
        if 'timeArea' in data:
            res.timeArea = data['timeArea']
        if 'isBuy' in data:
            res.isBuy = data['isBuy']
        if 'score' in data:
            res.score = data['score']
        if 'state' in data:
            res.state = data['state']
        if 'text' in data:
            res.text = data['text']
        res.save()

        return jsonify({'code': 0, 'data': [], 'message': 'CourseApi patch'})
