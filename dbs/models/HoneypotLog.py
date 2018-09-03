#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 蜜罐日志表
  Site: http://pirogue.org 
  Created: 2018-02-01 15:07:05
"""


from sqlalchemy import Column, String, Integer, Unicode, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship, backref
# import sys
# sys.path.append("..")
from dbs.initdb import Base, engine, DBSession


class OpencanaryLog(Base):
    __tablename__ = 'OpencanaryLog'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    dst_host = Column(String(50), nullable=False)
    dst_port = Column(Integer, nullable=False)
    honeycred = Column(Boolean, nullable=True)
    local_time = Column(TIMESTAMP, nullable=False)
    hostname = Column(String(50), nullable=True)
    password = Column(String(50), nullable=True)
    path = Column(Unicode(50), nullable=True)
    skin = Column(String(50), nullable=True)
    useragent = Column(Unicode(150), nullable=True)
    username = Column(String(50), nullable=True)
    session = Column(String(50), nullable=True)
    localversion = Column(String(50), nullable=True)
    remoteversion = Column(String(50), nullable=True)
    df = Column(String(30), nullable=True)
    idid = Column(String(20), nullable=True)
    inin = Column(String(50), nullable=True)
    lenlen = Column(String(50), nullable=True)
    mac = Column(String(60), nullable=True)
    outout = Column(String(50), nullable=True)
    prec = Column(String(20), nullable=True)
    proto = Column(String(10), nullable=True)
    res = Column(String(20), nullable=True)
    syn = Column(String(10), nullable=True)
    tos = Column(String(20), nullable=True)
    ttl = Column(String(20), nullable=True)
    urgp = Column(String(5), nullable=True)
    window = Column(String(50), nullable=True)
    logtype = Column(String(50), nullable=True)
    node_id = Column(String(30), nullable=False)
    src_host = Column(String(50), nullable=True)
    src_port = Column(Integer, nullable=False)
    white = Column(Integer, nullable=False)

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

if __name__=="__main__":
    init_db()
    print('create OpencanaryLog table')

"""
CREATE TABLE `OpencanaryLog` (
	id INTEGER NOT NULL AUTO_INCREMENT,
	dst_host VARCHAR(50) NOT NULL,
	dst_port INTEGER NOT NULL,
	honeycred BOOL,
	local_time TIMESTAMP NOT NULL,
	hostname VARCHAR(50),
	password VARCHAR(50),
	path VARCHAR(50),
	skin VARCHAR(50),
	useragent VARCHAR(150),
	username VARCHAR(50),
	session VARCHAR(50),
	localversion VARCHAR(50),
	remoteversion VARCHAR(50),
	df VARCHAR(30),
	idid VARCHAR(20),
	inin VARCHAR(50),
	lenlen VARCHAR(50),
	mac VARCHAR(60),
	outout VARCHAR(50),
	prec VARCHAR(20),
	proto VARCHAR(10),
	res VARCHAR(20),
	syn VARCHAR(10),
	tos VARCHAR(20),
	ttl VARCHAR(20),
	urgp VARCHAR(5),
	window VARCHAR(50),
	logtype VARCHAR(50),
	node_id VARCHAR(30) NOT NULL,
	src_host VARCHAR(50),
	src_port INTEGER NOT NULL,
	PRIMARY KEY (id),
	CHECK (honeycred IN (0, 1))
)

"""