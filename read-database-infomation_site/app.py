#!/usr/bin/env python3
# coding=utf-8
from pymongo import MongoClient
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from datetime import datetime

# 创建一个flask实例
app = Flask(__name__)

# 数据库的连接配置信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/infomation?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
db = SQLAlchemy(app, use_native_unicode="utf8")
mongo = MongoClient('127.0.0.1', 27017).news

# 创建一个内容表


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category')
    content = db.Column(db.Text)

    def __init__(self, title, category, content, created_time=None):
        self.title = title
        __table_args__ = {
                "mysql_charset": "utf8"
        }
        if created_time is None:
            created_time = datetime.utcnow()
        self.created_time = created_time
        self.category = category
        self.content = content

    # 增加tag函数
    def add_tag(self, tag):
        mongo.file.update_one({'_id': self.id}, {'$addToSet': {'tags': tag}})
        return self.__file['tags']

    # 删除tag函数
    def remove_tag(self, tag):
        mongo.file.update_one({'_id': self.id}, {'$pull': {'tags': tag}})
        return self.__file['tags']

    @property
    def __file(self):
        return mongo.file.find_one({'_id': self.id})

    @property
    def tags(self):
        return self.__file['tags']

    def __repr__(self):
        return '<File %r>' % self.title

# File 对象插入数据库时，自动创建关联的mongodb对象


@event.listens_for(File, 'after_insert')
def auto_create_mongodb_file(mapper, conn, file):
    mongo.file.insert_one({'_id': file.id})

# File 删除插入数据库时，自动创建关联的mongodb对象


@event.listens_for(File, 'after_delete')
def auto_delete_mongodb_file(mapper, conn, file):
    mongo.file.delete_one({'_id': file.id})

# 创建一个类别表


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        __table_args__ = {
                "mysql_charset": "utf8"
        }
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


# 网站路由

@app.route('/')
def index():
    return render_template('index.html', files=File.query.all())


@app.route('/files/<file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id)
    file_tag = mongo.file.find_one({'_id': int(file_id)})
    print(file_tag)
    return render_template(
        'file.html',
        file_item=file_item,
        file_tag=file_tag
    )



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
