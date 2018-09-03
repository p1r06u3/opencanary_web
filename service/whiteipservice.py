#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 白名单过滤
  Site: http://pirogue.org 
  Created: 2018-08-17 16:15:08
"""


from dbs.dal.Whiteip import White
# import sys
# sys.path.append("..")


White_res = White()

def whiteips():
    list_ip = []
    for ip in White_res.white_ip():
        list_ip.append(ip[0])
    return  list_ip