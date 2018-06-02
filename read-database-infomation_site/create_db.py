#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from  app import db, File, Category

#file1 = File('计算机语言简介','计算机语言','计算机语言有很多种，其中常见的有:Python,Java,Go,Shell...')
file2 = File('中国历史','历史','中华文化博大经深')

#db.session.add(file1)
db.session.add(file2)
db.session.commit()
