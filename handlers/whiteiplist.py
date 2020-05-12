#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 获取白名单ip
  Site: http://pirogue.org 
  Created: 2018-08-27 15:35:43
"""


import tornado
from handlers.base import BaseHandler
from util.auth import jwtauth
from service.whiteipservice import whiteips
# from dbs.dal.LogOperate import LogOp
import datetime
import json


@jwtauth
class WhiteiplistHandler(BaseHandler):
    """ 获取白名单ip列表 """

    def get(self):
        res = ','.join(whiteips())
        # json.dumps(line_res)
        self.write(res)
