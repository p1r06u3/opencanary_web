#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 后台面板首页路由
  Site: http://pirogue.org 
  Created: 2018-08-08 21:51:05
"""

import tornado
from util.auth import jwtauth
from handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        # Contains user found in previous auth
        self.render('index.html')

    def post(self):
    # Contains user found in previous auth
      self.render('index.html')