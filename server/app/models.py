# !usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:Mckay
@file: models.py.py
@time: 2019/12/12
"""
import datetime
from flask_mongoengine import MongoEngine

db = MongoEngine()


class Todo(db.Document):
    title = db.StringField(max_length=60)
    text = db.StringField()
    done = db.BooleanField(default=False)
    pub_date = db.DateTimeField(default=datetime.datetime.now)


# class ExamInfo(db.Document):


# 试卷库-关联题目
class Paper(db.Document):
    name = db.StringField()
    courseId = db.IntField()
    type = db.IntField()
    timeType = db.IntField()
    timeAll = db.IntField()
    text = db.StringField()


# 试题库-题目
class Question(db.Document):
    courseId = db.IntField()
    typeId = db.IntField()
    grade = db.IntField()
    subject = db.StringField()
    answer = db.StringField()
    tag = db.StringField()
    text = db.StringField()


# 课程-分类
class CCategory(db.Document):
    # 学校，职能，自考
    name = db.StringField(max_length=60)
    parentId = db.IntField()
    text = db.StringField()


# 课程-列表
class Course(db.Document):
    # id = db.StringField(primary_key=True)
    name = db.StringField(max_length=60)
    CourseCategoryId = db.IntField()
    img = db.StringField()
    timeArea = db.StringField()
    isBuy = db.BooleanField(default=False)
    score = db.IntField(default=0)
    state = db.BooleanField(default=True)
    text = db.StringField()


# 知识库
class Wiki(db.Document):
    name = db.StringField(max_length=60)
    CourseCategoryId = db.IntField()
    type = db.IntField()
    tag = db.StringField()
    source = db.StringField()
    text = db.StringField()


# 用户信息
class User(db.Document):
    name = db.StringField(max_length=60)
    email = db.EmailField()
    phone = db.StringField()
    text = db.StringField()
    wx = db.StringField()
    courses = db.StringField()
    score = db.StringField()


# StringField
# BinaryField
# URLField
# EmailField
# IntField
# FloatField
# DecimalField
# BooleanField
# DateTimeField
# ListField (using wtforms.fields.FieldList )
# SortedListField (duplicate ListField)
# EmbeddedDocumentField (using wtforms.fields.FormField and generating inline Form)
# ReferenceField (using wtforms.fields.SelectFieldBase with options loaded from QuerySet or Document)
# DictField
