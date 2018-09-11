#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 白名单端口过滤
  Site: http://pirogue.org 
  Created: 2018-08-17 16:15:08
"""


from dbs.dal.Whiteport import WhitePort
# import sys
# sys.path.append("..")


White_res = WhitePort()

def whiteports():
    list_port = []
    for port in White_res.select_white_port():
        list_port.append(port[0])
    return list_port


def insertports(list_port):
    for p in list_port:
        if p:
            White_res.insert_white_port(int(p))
    return True

def deleteports():
    White_res.delete_white_port()
    return True