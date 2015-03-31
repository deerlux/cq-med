# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy.ext.automap import automap_base
import sqlalchemy
from sqlalchemy.orm import Session

from singleton import singleton

# 此类是个单实例类，提供数据库的操作接口
@singleton
class MedDB:

    def __init__(self, engine_str = 'postgresql://localhost/medical'):
        self.engine_str = engine_str
        engine = sqlalchemy.create_engine(self.engine_str)
        self.session = Session(engine)

        self.Base = automap_base()
        self.Base.prepare(engine, reflect=True)

        self.Jianchazhibiao = self.Base.classes.jianchazhibiao
        self.query = self.session.query


    def __del__(self):
        self.session.close()

