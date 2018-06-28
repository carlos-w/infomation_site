#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from app import db, File, Category
# 创建所有表
db.create_all()
# 在类别表中插入数据
cate1 = Category('Java')
cate2 = Category('Python')
db.session.add(cate1)
db.session.add(cate2)
db.session.commit()
# 在文件表中插入数据

file1 = File('Hello Java', cate1, 'File Content - Java is cool!')
file2 = File('Hello Python', cate2, 'File Cntent - Python is cool!')
db.session.add(file1)
db.session.add(file2)
db.session.commit()

file1.add_tag('tech')
file1.add_tag('java')
file1.add_tag('linux')
file2.add_tag('tech')
file2.add_tag('python')
