#!/bin/env python2
from __future__ import print_function

from sqlalchemy.ext.automap import automap_base
import sqlalchemy
from sqlalchemy.orm import Session
import csv

if __name__ == '__main__':
    
    engine_str = 'postgresql://localhost/medical'
    engine = sqlalchemy.create_engine(engine_str)
    session = Session(engine)

    Base = automap_base()
    Base.prepare(engine, reflect=True)

    Jianchazhibiao = Base.classes.jianchazhibiao

    
    filename = 'initdata.csv'
    f1 = open(filename,'r')
    reader = csv.reader(f1)

    for k,v in enumerate(reader):
        if k == 0:
            continue
        for i,cell in enumerate(v):
            if cell == '':
                v[i] = None
        item = Jianchazhibiao(zhibiao_name=v[0],
                zhibiao_name_eng = v[1],
                zhibiao_ref1 = v[2],
                zhibiao_ref2 = v[3],
                zhibiao_unit = v[4])
        session.add(item)

    session.commit()
    
    print('{0} records imported.'.format(k))

    session.close()

