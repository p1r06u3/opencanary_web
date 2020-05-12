#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 数据库配置文件
  Site: http://pirogue.org 
  Created: 2018-02-01 15:04:29
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 数据库配置
DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PWD = 'JDWP@jdwp'
DB_NAME = 'honeypot'

# 创建对象基类
Base = declarative_base()

# 初始化数据库连接
engine = create_engine('mysql+pymysql://%s:%s@%s/%s?charset=utf8' %
                       (DB_USER, DB_PWD, DB_HOST, DB_NAME),
                   encoding='utf-8', echo=True,
                 pool_size=100, pool_pre_ping=True, pool_recycle=3600)

# 创建DBsession类型
Session = sessionmaker(bind=engine)
DBSession = Session()
