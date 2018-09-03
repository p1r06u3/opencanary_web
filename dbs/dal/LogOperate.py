#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 日志表操作
  Site: http://pirogue.org 
  Created: 2018-08-03 17:32:54
"""

from dbs.initdb import DBSession
from dbs.models.HoneypotLog import OpencanaryLog
from dbs.models.Whiteip import Whiteip
from sqlalchemy import desc,asc,extract,func,distinct


class LogOp:
    """增删改查"""

    def __init__(self):  
        self.session=DBSession

    def insert(self, dst_host, dst_port, honeycred, local_time, hostname, password, path, skin,\
             useragent, username, session, localversion, remoteversion, df, idid, inin, lenlen, mac, outout,\
             prec, proto, res, syn, tos, ttl, urgp, window, logtype, node_id, src_host, src_port, white):

        loginsert = OpencanaryLog(dst_host=dst_host, dst_port=dst_port, honeycred=honeycred, local_time=local_time,\
            hostname=hostname, password=password, path=path, skin=skin, useragent=useragent, username=username,\
            session=session, localversion=localversion, remoteversion=remoteversion, df=df, idid=idid, inin=inin,\
            lenlen=lenlen, mac=mac, outout=outout, prec=prec, proto=proto, res=res, syn=syn, tos=tos, ttl=ttl,\
            urgp=urgp, window=window, logtype=logtype, node_id=node_id, src_host=src_host, src_port=src_port, white=white)
            
        if loginsert:

            self.session.add(loginsert)
            self.session.commit()
            self.session.close()
            return True
        else:
            return False

    # 查询日志表攻击列表数据
    def page_select_attack(self, page_index):
        page_size = 10
        # num = 10*int(page) - 10
        logselect = self.session.query(OpencanaryLog).filter(OpencanaryLog.white==2).order_by(desc(OpencanaryLog.local_time),OpencanaryLog.id).limit(page_size).offset((page_index-1)*page_size)
        self.session.close()
        return logselect

    # 查询日志表白名单数据
    def page_select_white(self, page_index):
        page_size = 10
        # num = 10*int(page) - 10
        logselect = self.session.query(OpencanaryLog).filter(OpencanaryLog.white==1).order_by(desc(OpencanaryLog.local_time),OpencanaryLog.id).limit(page_size).offset((page_index-1)*page_size)
        self.session.close()
        return logselect

    # 查询当年每月攻击数量
    def attack_select_num(self, months):
        attack_num = self.session.query(extract('month', OpencanaryLog.local_time).label('month'), func.count('*').label('count')).filter(extract('year', OpencanaryLog.local_time) == months, OpencanaryLog.white==2).group_by('month').all()
        self.session.close()
        return attack_num

    # 查询当年每月白名单内攻击数量
    def white_select_num(self, months):
        white_num = self.session.query(extract('month', OpencanaryLog.local_time).label('month'), func.count('*').label('count')).filter(extract('year', OpencanaryLog.local_time) == months, OpencanaryLog.white==1).group_by('month').all()
        self.session.close()
        return white_num
    
    # 查询各类攻击数量
    def pie_select_num(self, years):
        pie_num = self.session.query(func.count(OpencanaryLog.logtype),OpencanaryLog.logtype).group_by(OpencanaryLog.logtype).filter(extract('year', OpencanaryLog.local_time) == years, OpencanaryLog.white==2).all()
        self.session.close()
        return pie_num