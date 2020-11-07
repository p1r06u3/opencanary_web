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
import sys
sys.path.append("..")
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
    useragent = Column(Unicode(250), nullable=True)
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
    ## 扩表
    repo = Column(String(150), nullable=True)
    ntp_cmd = Column(String(150), nullable=True)
    args = Column(String(150), nullable=True)
    cmd = Column(String(150), nullable=True)
    banner_id = Column(String(30), nullable=True)
    data = Column(String(150), nullable=True)
    function = Column(String(150), nullable=True)
    vnc_client_response = Column(String(150), nullable=True)
    vnc_password = Column(String(50), nullable=True)
    vnc_server_challenge = Column(String(150), nullable=True)
    inputs = Column(String(150), nullable=True)
    domain = Column(String(150), nullable=True)
    headers_call_id = Column(String(150), nullable=True)
    headers_content_length = Column(String(150), nullable=True)
    headers_cseq = Column(String(150), nullable=True)
    headers_from = Column(String(150), nullable=True)
    headers_to = Column(String(150), nullable=True)
    headers_via = Column(String(150), nullable=True)
    community_string = Column(String(50), nullable=True)
    requests = Column(String(50), nullable=True)
    urg = Column(String(50), nullable=True)
    psh = Column(String(50), nullable=True)
    fin = Column(String(50), nullable=True)
    appname = Column(String(150), nullable=True)
    cltintname = Column(String(150), nullable=True)
    database = Column(String(50), nullable=True)
    language = Column(String(50), nullable=True)
    servername = Column(String(50), nullable=True)
    domainname = Column(String(50), nullable=True)


def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

if __name__=="__main__":
    init_db()
    print('create OpencanaryLog table')

    # drop_db()
    # print('Drop OpencanaryLog table')
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
	useragent VARCHAR(250),
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
	`window` VARCHAR(50),
	logtype VARCHAR(50),
	node_id VARCHAR(30) NOT NULL,
	src_host VARCHAR(50),
	src_port INTEGER NOT NULL,
	white INTEGER NOT NULL,
	repo VARCHAR(150),
	ntp_cmd VARCHAR(150),
	args VARCHAR(150),
	cmd VARCHAR(150),
	banner_id VARCHAR(30),
	data VARCHAR(150),
	function VARCHAR(150),
	vnc_client_response VARCHAR(150),
	vnc_password VARCHAR(50),
	vnc_server_challenge VARCHAR(150),
	inputs VARCHAR(150),
	domain VARCHAR(150),
	headers_call_id VARCHAR(150),
	headers_content_length VARCHAR(150),
	headers_cseq VARCHAR(150),
	headers_from VARCHAR(150),
	headers_to VARCHAR(150),
	headers_via VARCHAR(150),
	community_string VARCHAR(50),
	requests VARCHAR(50),
	urg VARCHAR(50),
	psh VARCHAR(50),
	fin VARCHAR(50),
	appname VARCHAR(150),
	cltintname VARCHAR(150),
	`database` VARCHAR(50),
	language VARCHAR(50),
	servername VARCHAR(50),
	domainname VARCHAR(50),
	PRIMARY KEY (id),
	CHECK (honeycred IN (0, 1))
)
"""