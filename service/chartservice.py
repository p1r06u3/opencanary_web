#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 折线图和饼图
  Site: http://pirogue.org 
  Created: 2018-08-27 18:29:06
"""

from dbs.dal.LogOperate import LogOp
import datetime
import sys
from importlib import reload
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding('utf8')

nums = LogOp()



# sourceDataz = [
# { "month": 'Jan', "attack": 0, "white": 0 },
# { "month": 'Feb', "attack": 0, "white": 0 },
# { "month": 'Mar', "attack": 0, "white": 0 },
# { "month": 'Apr', "attack": 0, "white": 0 },
# { "month": 'May', "attack": 0, "white": 0 },
# { "month": 'Jun', "attack": 0, "white": 0 },
# { "month": 'Jul', "attack": 0, "white": 0 },
# { "month": 'Aug', "attack": 0, "white": 0 },
# { "month": 'Sep', "attack": 0, "white": 0 },
# { "month": 'Oct', "attack": 0, "white": 0 },
# { "month": 'Nov', "attack": 0, "white": 0 },
# { "month": 'Dec', "attack": 0, "white": 0 },
# ]


def attack_num(sourceDataz):
    """ 每月攻击数量统计 """
    # 当前的年份
    now = datetime.datetime.now().year
    now=2019
    attack_res = nums.attack_select_num(now)
    print("attack_res:"+str(attack_res))
    # [(5, 1), (7, 2), (8, 258), (9, 3)]
    if attack_res:
        for at in attack_res:
            if at[0] == 1:
                sourceDataz[0]["attack"] = at[1]
            elif at[0] == 2:
                sourceDataz[1]["attack"] = at[1]
            elif at[0] == 3:
                sourceDataz[2]["attack"] = at[1]
            elif at[0] == 4:
                sourceDataz[3]["attack"] = at[1]
            elif at[0] == 5:
                sourceDataz[4]["attack"] = at[1]
            elif at[0] == 6:
                sourceDataz[5]["attack"] = at[1]
            elif at[0] == 7:
                sourceDataz[6]["attack"] = at[1]
            elif at[0] == 8:
                sourceDataz[7]["attack"] = at[1]
            elif at[0] == 9:
                sourceDataz[8]["attack"] = at[1]
            elif at[0] == 10:
                sourceDataz[9]["attack"] = at[1]
            elif at[0] == 11:
                sourceDataz[10]["attack"] = at[1]
            elif at[0] == 12:
                sourceDataz[11]["attack"] = at[1]
        # print sourceDataz
    return sourceDataz


def white_num(sourceDataz):
    """ 每月白名单攻击数量统计 """
    # 当前的年份
    now = datetime.datetime.now().year
    white_res = nums.white_select_num(now)
    # [(5, 1), (7, 2), (8, 258), (9, 3)]
    if white_res:
        for at in white_res:
            if at[0] == 1:
                sourceDataz[0]["white"] = at[1]
            elif at[0] == 2:
                sourceDataz[1]["white"] = at[1]
            elif at[0] == 3:
                sourceDataz[2]["white"] = at[1]
            elif at[0] == 4:
                sourceDataz[3]["white"] = at[1]
            elif at[0] == 5:
                sourceDataz[4]["white"] = at[1]
            elif at[0] == 6:
                sourceDataz[5]["white"] = at[1]
            elif at[0] == 7:
                sourceDataz[6]["white"] = at[1]
            elif at[0] == 8:
                sourceDataz[7]["white"] = at[1]
            elif at[0] == 9:
                sourceDataz[8]["white"] = at[1]
            elif at[0] == 10:
                sourceDataz[9]["white"] = at[1]
            elif at[0] == 11:
                sourceDataz[10]["white"] = at[1]
            elif at[0] == 12:
                sourceDataz[11]["white"] = at[1]
    return sourceDataz


def line_total_num(sdataz):
    data_attack = attack_num(sdataz)
    # print data_attack
    data_attack_white = white_num(data_attack)
    # print data_attack_white
    return data_attack_white


# this.sourceData = [
#   { item: 'ftp', count: 40 },
#   { item: 'http', count: 21 },
#   { item: 'ssh', count: 17 },
#   { item: 'telnet', count: 13 },
#   { item: 'portscan', count: 9 },
#   { item: 'mysql', count: 0 }
# ];


def pie_num(piesoureData):
    # 当前的年份
    now = datetime.datetime.now().year
    """ 饼图数据 """
    now=2019
    data_pie = nums.pie_select_num(now)
    print(data_pie)
    if data_pie:
        for p in data_pie:
            if p[1] == '2000':
                piesoureData[0]["count"] = int(p[0])
            elif p[1] == '3000' or p[1] == '3001':
                piesoureData[1]["count"] = piesoureData[1]["count"] + int(p[0])
            elif p[1] == '4000' or p[1] == '4001' or p[1] == '4002':
                piesoureData[2]["count"] = piesoureData[2]["count"] + int(p[0])
            elif p[1] == '6001':
                piesoureData[3]["count"] = int(p[0])
            elif p[1] == '5001' or p[1] == '5002' or p[1] == '5003' or p[1] == '5004' or p[1] == '5005':
                piesoureData[4]["count"] = piesoureData[4]["count"] + int(p[0])
            elif p[1] == '8001':
                piesoureData[5]["count"] = int(p[0])
            elif p[1] == '16001':
                piesoureData[6]["count"] = int(p[0])
            elif p[1] == '11001':
                piesoureData[7]["count"] = int(p[0])
            elif p[1] == '17001':
                piesoureData[8]["count"] = int(p[0])
            elif p[1] == '18001' or p[1] == '18002' or p[1] == '18003' or p[1] == '18004' or p[1] == '18005':
                piesoureData[9]["count"] = piesoureData[9]["count"] + int(p[0])
            elif p[1] == '12001':
                piesoureData[10]["count"] = int(p[0])
            elif p[1] == '14001':
                piesoureData[11]["count"] = int(p[0])
            elif p[1] == '13001':
                piesoureData[12]["count"] = int(p[0])
            elif p[1] == '15001':
                piesoureData[13]["count"] = int(p[0])
            elif p[1] == '9001' or p[1] == '9002':
                piesoureData[14]["count"] = piesoureData[14]["count"] + int(p[0])
            elif p[1] == '7001':
                piesoureData[15]["count"] = int(p[0])
    return piesoureData
