#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# 创建一个flask实例
app = Flask(__name__)
# 数据库的连接配置信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/infomation'
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

# 创建一个内容表

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)

    def __init__(self,title,category_id,content,created_time=None):
        self.title = title
        if created_time is None:
            create_time = datetime.utcnow()
        self.create_time = create_time
        self.category_id = category_id
        self.content = content

    def __repr__(self):
        return '<File %r>' % self.title
# 创建一个类别表

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name



