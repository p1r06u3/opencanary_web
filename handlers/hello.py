#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 测试认证请求里的token
  Site: http://pirogue.org 
  Created: 2018-08-07 20:56:24
"""

import tornado
from util.auth import jwtauth
from handlers.base import BaseHandler
from service.hostservice import hostonline

# @jwtauth
class HelloHandler(BaseHandler):
    def get(self):
        print(hostonline())
        # self.write(str(hostonline()))
        self.write("ok")

        # Contains user found in previous auth
        # if self.request.headers.get('Authorization'):
        #     self.write('ok')
