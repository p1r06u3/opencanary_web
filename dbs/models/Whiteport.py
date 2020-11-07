#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 蜜罐白名单端口表
  Site: http://pirogue.org 
  Created: 2018-02-01 15:07:05
"""


from sqlalchemy import Column, String, Integer, Unicode, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship, backref
# import sys
# sys.path.append("..")
from dbs.initdb import Base, engine, DBSession


class Whiteport(Base):
    __tablename__ = 'Whiteport'
    dst_port = Column(Integer, nullable=False, primary_key=True)


def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

if __name__=="__main__":
    init_db()
    #drop_db()
    # Whiteport_data = Whiteport()
    # Whiteport_data.dsr_port = 3306
    # DBSession.add(Whiteport_data)
    # DBSession.flush()
    # DBSession.commit()
    print('create Whiteport table')