#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 路由请求基础类
  Site: http://pirogue.org 
  Created: 2018-08-07 16:03:41
"""


import tornado
import json

class BaseHandler(tornado.web.RequestHandler):
        #----------------------------------------------------------------------
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*') # 这个地方可以写域名
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.set_header("Server","Apache-Coyote/1.1")

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('index.html')
        elif status_code == 500:
            self.render('index.html')
        else:
            self.write('error:' + str(status_code))
    # def prepare(self):
    
    #     self.set_header("Server","Apache-Coyote/1.1")
    #     if self.request.arguments:
    #         pass
    #     else:
    #         self.send_error(status_code=400)
        # if self.request.headers["Content-Type"].startswith("application/json"):
        #     self.json_args = json.loads(self.request.body)
        # else:
        #     self.json_args = None
        #     message = 'Unable to parse JSON.'
        #     self.send_error(status_code=400) # 向浏览器发送错误状态码，会调用write_error