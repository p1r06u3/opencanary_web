#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 日志列表分页
  Site: http://pirogue.org 
  Created: 2018-08-06 18:33:29
"""


import tornado
import json
from service.paginationlog import listpage
from base import BaseHandler
from util.auth import jwtauth

@jwtauth
class GetlistJsonHandler(BaseHandler):
    """ 获取日志列表 """

    # 自定义错误页面
    def write_error(self,status_code,**kwargs):
        self.write("Unable to parse JSON.")

    def post(self):
        # 
        if self.request.headers["Content-Type"].startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None
            message = 'Unable to parse JSON.'
            self.send_error(status_code=400) # 向浏览器发送错误状态码，会调用write_error

        param = self.request.body.decode('utf-8')
        print 'page start'

        # print type(param)
        
        param = json.loads(param)
        # print param
        viewres = listpage(param)
        # print param
        # print(type(param))
        self.write(viewres)
    
    def get(self):
        self.write('get ok')

