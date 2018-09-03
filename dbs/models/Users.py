#!/usr/bin/env python
#coding:utf-8
"""
  Author:  pirogue --<p1r06u3@gmail.com>
  Purpose: 用户关系模型
  Created: 2018年08月07日16:48:39
  Site:    http://pirogue.org
"""


from datetime import datetime
from sqlalchemy import Column, String, Integer, Unicode, TIMESTAMP
from sqlalchemy.orm import relationship, backref
# import sys
# sys.path.append("..")
from dbs.initdb import Base, engine, DBSession


class User(Base):
    __tablename__ = 'User'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(32), nullable=False)
    create_time = Column(TIMESTAMP, default=datetime.now)

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

if __name__=="__main__":
    init_db()
    #drop_db()
    # user_data = User()
    # user_data.username = 'admin'
    # user_data.email = ''
    # user_data.password = '21232f297a57a5a743894a0e4a801fc3'
    # DBSession.add(user_data)
    # DBSession.flush()
    # DBSession.commit()
    print('create user table')



'''
    CREATE TABLE `User` (
	id INTEGER NOT NULL AUTO_INCREMENT,
	username VARCHAR(50) NOT NULL,
	password VARCHAR(32) NOT NULL,
	create_time TIMESTAMP NULL,
	PRIMARY KEY (id)
    )
INSERT INTO `User` (username, password, create_time) VALUES (%(username)s, %(password)s, %(create_time)s)
{'username': 'admin', 'password': '21232f297a57a5a743894a0e4a801fc3', 'create_time': datetime.datetime(2018, 8, 7, 16, 52, 44, 676617)}
'''