#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from  app import db, File, Category

#file1 = File('��������Լ��','���������','����������кܶ��֣����г�������:Python,Java,Go,Shell...')
file2 = File('�й���ʷ','��ʷ','�л��Ļ�������')

#db.session.add(file1)
db.session.add(file2)
db.session.commit()
