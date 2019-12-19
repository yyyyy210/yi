# !usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:Mckay
@file: articles.py.py
@time: 2019/12/12
"""
from flask import jsonify, request
from flask_restful import Resource
from ..models import User


class UserApi(Resource):
    def get(self):
        lists = User.objects.all()
        return jsonify({'code': 0, 'data': lists, 'message': 'UserApi get'})

    def post(self):
        data = request.json
        res = User(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            text=data['text'],
            wx=data['wx'],
            courses=data['courses'],
            score=data['score']
        ).save()
        return jsonify({'code': 0, 'data': res, 'message': 'UserApi post ' + str(data['name'])})

    def delete(self, user_id):
        if not user_id:
            return jsonify({'code': 1, 'data': [], 'message': 'UserApi del not user_id'})
        try:
            res = User.objects(id=user_id)
            res.delete()
            return jsonify({'code': 0, 'data': [], 'message': 'UserApi del'})
        except:
            return jsonify({'code': 1, 'data': [], 'message': 'UserApi del sql not user_id'})

    def patch(self, user_id):
        data = request.json
        res = User.objects.get(id=user_id)
        if 'name' in data:
            res.name = data['name']
        if 'email' in data:
            res.email = data['email']
        if 'phone' in data:
            res.phone = data['phone']
        if 'text' in data:
            res.text = data['text']
        if 'wx' in data:
            res.wx = data['wx']
        if 'courses' in data:
            res.courses = data['courses']
        if 'score' in data:
            res.score = data['score']
        res.save()

        return jsonify({'code': 0, 'data': [], 'message': 'UserApi patch'})
