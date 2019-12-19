# !usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:Mckay
@file: articles.py.py
@time: 2019/12/12
"""
from flask import jsonify, request
from flask_restful import Resource
from ..models import Question


class QuestionApi(Resource):
    def get(self):
        lists = Question.objects.all()
        return jsonify({'code': 0, 'data': lists, 'message': 'QuestionApi get'})

    def post(self):
        data = request.json
        res = Question(
            courseId=data['courseId'],
            typeId=data['typeId'],
            grade=data['grade'],
            subject=data['subject'],
            answer=data['answer'],
            tag=data['tag'],
            text=data['text']
        ).save()
        return jsonify({'code': 0, 'data': res, 'message': 'QuestionApi post ' + str(data['subject'])})

    def delete(self, question_id):
        if not question_id:
            return jsonify({'code': 1, 'data': [], 'message': 'QuestionApi del not Question_id'})
        try:
            res = Question.objects(id=question_id)
            res.delete()
            return jsonify({'code': 0, 'data': [], 'message': 'QuestionApi del'})
        except:
            return jsonify({'code': 1, 'data': [], 'message': 'QuestionApi del sql not Question_id'})

    def patch(self, question_id):
        data = request.json
        res = Question.objects.get(id=question_id)
        if 'courseId' in data:
            res.courseId = data['courseId']
        if 'typeId' in data:
            res.typeId = data['typeId']
        if 'grade' in data:
            res.grade = data['grade']
        if 'subject' in data:
            res.subject = data['subject']
        if 'answer' in data:
            res.answer = data['answer']
        if 'tag' in data:
            res.tag = data['tag']
        if 'text' in data:
            res.text = data['text']
        res.save()

        return jsonify({'code': 0, 'data': [], 'message': 'QuestionApi patch'})
