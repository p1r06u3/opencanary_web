#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: dashboard charts
  Site: http://pirogue.org 
  Created: 2018-08-27 15:35:43
"""


import tornado
from handlers.base import BaseHandler
from util.auth import jwtauth
from service.chartservice import line_total_num, pie_num
# from dbs.dal.LogOperate import LogOp
import datetime
import json


@jwtauth
class ChartHandler(BaseHandler):
    """ 获取日志列表 """

    def get(self):
        #print("test1")
        #print("MARK: ")
        charts = "line" in self.request.arguments
        #print(charts)
        if charts:
            sourceDataz = [
            { "month": 'Jan', "attack": 0, "white": 0 },
            { "month": 'Feb', "attack": 0, "white": 0 },
            { "month": 'Mar', "attack": 0, "white": 0 },
            { "month": 'Apr', "attack": 0, "white": 0 },
            { "month": 'May', "attack": 0, "white": 0 },
            { "month": 'Jun', "attack": 0, "white": 0 },
            { "month": 'Jul', "attack": 0, "white": 0 },
            { "month": 'Aug', "attack": 0, "white": 0 },
            { "month": 'Sep', "attack": 0, "white": 0 },
            { "month": 'Oct', "attack": 0, "white": 0 },
            { "month": 'Nov', "attack": 0, "white": 0 },
            { "month": 'Dec', "attack": 0, "white": 0 },
            ]
            line_res = line_total_num(sourceDataz)
            # print line_res
            # print json.dumps(line_res)
            self.write(json.dumps(line_res))
        else:
            sourceData = [
                { "item": 'ftp', "count": 0 },
                { "item": 'http', "count": 0 },
                { "item": 'ssh', "count": 0 },
                { "item": 'telnet', "count": 0 },
                { "item": 'portscan', "count": 0 },
                { "item": 'mysql', "count": 0 },
                { "item": 'git', "count": 0 },
                { "item": 'ntp', "count": 0 },
                { "item": 'redis', "count": 0 },
                { "item": 'tcpbanner', "count": 0 },
                { "item": 'vnc', "count": 0 },
                { "item": 'rdp', "count": 0 },
                { "item": 'snmp', "count": 0 },
                { "item": 'sip', "count": 0 },
                { "item": 'mssql', "count": 0 },
                { "item": 'httpproxy', "count": 0 }
            ]
            pie_res = pie_num(sourceData)
            self.write(json.dumps(pie_res))
        #self.finish()
