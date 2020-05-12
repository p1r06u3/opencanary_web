#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 接收客户端请求
  Site: http://pirogue.org 
  Created: 2018-01-31 18:36:39
"""


import tornado
import json
from service.splitjsonlog import parserlog
from service.paginationlog import listpage
from handlers.base import BaseHandler
from util.auth import jwtauth
from service.emailservice import send_mail


# @jwtauth
class ReceiveJsonHandler(BaseHandler):
    """ 接收客户端的日志post json请求 """

    #----------------------------------------------------------------------
    
    # 自定义错误页面
    def write_error(self,status_code,**kwargs):
        self.write("Unable to parse JSON.")

    def prepare(self):
        self.set_header("Server","Apache-Coyote/1.1")
        if self.request.headers["Content-Type"].startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None
            message = 'Unable to parse JSON.'
            self.send_error(status_code=400) # 向浏览器发送错误状态码，会调用write_error


    def post(self):
        # 接收post json客户端蜜罐日志
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        # print param
        # print(type(param))
        parserlog(param)

        self.write(param)
    
    def get(self):
        self.write('get ok')


