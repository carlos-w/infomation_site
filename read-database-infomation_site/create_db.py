#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from  app import db, File, Category

cate1 = Category('计算机语言2')
cate2 = Category('历史2')

db.session.add(cate1)
db.session.add(cate2)
db.session.commit()
file1 = File('计算机语言简介2',cate1,'计算机语言有很多种，其中常见的有:Python,Java,Go,Shell...')
file2 = File('中国历史2',cate2,'中华文化博大经深')
db.session.add(file1)
db.session.add(file2)
db.session.commit()
