#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 解析客户端请求过来的日志
  Site: http://pirogue.org 
  Created: 2018-08-03 18:00:23
"""

from dbs.dal.LogOperate import LogOp
import datetime
from service.emailservice import send_mail,switches
from service.whiteipservice import whiteips

loginst = LogOp()

def parserlog(jsonlog):
    # 接收客户端post过来的数据格式化
    if jsonlog:
        if jsonlog.has_key("dst_host"):
            dst_host = jsonlog["dst_host"]
            # print type(dst_host)
        else:
            dst_host = ''

        if jsonlog.has_key("dst_port"):
            dst_port = jsonlog["dst_port"]
        else:
            dst_port = 0

        if jsonlog.has_key("honeycred"):
            honeycred = jsonlog["honeycred"]
        else:
            honeycred = False

        if jsonlog.has_key("local_time"):
            local_time = jsonlog["local_time"]
            print local_time
        else:
            local_time = datetime.datetime.now()

        if jsonlog.has_key("logdata"):
            if jsonlog["logdata"].has_key("HOSTNAME"):
                hostname = jsonlog["logdata"]["HOSTNAME"]
            else:
                hostname = ''

            if jsonlog["logdata"].has_key("PASSWORD"):
                password = jsonlog["logdata"]["PASSWORD"]
            else:
                password = ''

            if jsonlog["logdata"].has_key("PATH"):
                path = jsonlog["logdata"]["PATH"]
            else:
                path = ''

            if jsonlog["logdata"].has_key("SKIN"):
                skin = jsonlog["logdata"]["SKIN"]
            else:
                skin = ''

            if jsonlog["logdata"].has_key("USERAGENT"):
                useragent = jsonlog["logdata"]["USERAGENT"]
            else:
                useragent = ''

            if jsonlog["logdata"].has_key("USERNAME"):
                username = jsonlog["logdata"]["USERNAME"]
            else:
                username = ''

            if jsonlog["logdata"].has_key("SESSION"):
                session = jsonlog["logdata"]["SESSION"]
            else:
                session = ''

            if jsonlog["logdata"].has_key("LOCALVERSION"):
                localversion = jsonlog["logdata"]["LOCALVERSION"]
            else:
                localversion = ''

            if jsonlog["logdata"].has_key("REMOTEVERSION"):
                remoteversion = jsonlog["logdata"]["REMOTEVERSION"]
            else:
                remoteversion = ''

            if jsonlog["logdata"].has_key("DF"):
                df = jsonlog["logdata"]["DF"]
            else:
                df = '' 

            if jsonlog["logdata"].has_key("ID"):
                idid = jsonlog["logdata"]["ID"]
            else:
                idid = ''

            if jsonlog["logdata"].has_key("IN"):
                inin = jsonlog["logdata"]["IN"]
            else:
                inin = ''

            if jsonlog["logdata"].has_key("LEN"):
                lenlen = jsonlog["logdata"]["LEN"]
            else:
                lenlen = ''

            if jsonlog["logdata"].has_key("MAC"):
                mac = jsonlog["logdata"]["MAC"]
            else:
                mac = ''

            if jsonlog["logdata"].has_key("OUT"):
                outout = jsonlog["logdata"]["OUT"]
            else:
                outout = ''

            if jsonlog["logdata"].has_key("PREC"):
                prec = jsonlog["logdata"]["PREC"]
            else:
                prec = ''

            if jsonlog["logdata"].has_key("PROTO"):
                proto = jsonlog["logdata"]["PROTO"]
            else:
                proto = ''

            if jsonlog["logdata"].has_key("RES"):
                res = jsonlog["logdata"]["RES"]
            else:
                res = ''

            if jsonlog["logdata"].has_key("SYN"):
                syn = jsonlog["logdata"]["SYN"]
            else:
                syn = ''

            if jsonlog["logdata"].has_key("TOS"):
                tos = jsonlog["logdata"]["TOS"]
            else:
                tos = ''

            if jsonlog["logdata"].has_key("TTL"):
                ttl = jsonlog["logdata"]["TTL"]
            else:
                ttl = ''

            if jsonlog["logdata"].has_key("URGP"):
                urgp = jsonlog["logdata"]["URGP"]
            else:
                urgp = ''

            if jsonlog["logdata"].has_key("WINDOW"):
                window = jsonlog["logdata"]["WINDOW"]
            else:
                window = ''
        else:
                hostname = ''
                password = ''
                path = ''
                skin = ''
                useragent = ''
                username = ''
                session = ''
                localversion = ''
                remoteversion = ''
                df = '' 
                idid = ''
                inin = ''
                lenlen = ''
                mac = ''
                outout = ''
                prec = ''
                proto = ''
                res = ''
                syn = ''
                tos = ''
                ttl = ''
                urgp = ''
                window = ''

        if jsonlog.has_key("logtype"):
            logtype = jsonlog["logtype"]
        else:
            logtype = ''

        if jsonlog.has_key("node_id"):
            node_id = jsonlog["node_id"]
        else:
            node_id = ''

        if jsonlog.has_key("src_host"):
            src_host = jsonlog["src_host"]
        else:
            src_host = ''

        if jsonlog.has_key("src_port"):
            src_port = jsonlog["src_port"]
        else:
            src_port = 0
        if dst_host:
            if src_host:
                # 判断攻击主机是否存在于白名单列表内
                if src_host in whiteips():
                    # 存在将white字段设置为1
                    white = 1
                else:
                    # 不存在将white字段设置为2
                    white = 2
                # 将客户端post过来的数据插入数据库
                logbool = loginst.insert(dst_host, dst_port, honeycred, local_time, hostname, password, path, skin,\
                    useragent, username, session, localversion, remoteversion, df, idid, inin, lenlen, mac, outout,\
                    prec, proto, res, syn, tos, ttl, urgp, window, logtype, node_id, src_host, src_port, white)
                if logbool and white == 2:
                    # 发送邮件功能
                    if switches() =='on':
                        if str(logtype) =='2000':
                            logtype = 'ftp登录尝试'
                        elif str(logtype) == '3000':
                            logtype = 'web蜜罐被访问'
                        elif str(logtype) == '3001':
                            logtype = 'web蜜罐被登录'
                        elif str(logtype) == '4000':
                            logtype = 'ssh建立连接'
                        elif str(logtype) == '4001':
                            logtype = 'ssh远程版本发送'
                        elif str(logtype) == '4002':
                            logtype = 'ssh登录尝试'
                        elif str(logtype) == '6001':
                            logtype = 'telnet登录尝试'
                        elif str(logtype) == '5001':
                            logtype = '端口扫描行为'
                        elif str(logtype) == '8001':
                            logtype = 'mysql登录尝试'
                        content = "攻击主机："+src_host+"--"+"被攻击主机："+dst_host+"--"+"攻击时间："+local_time
                        send_mail("蜜罐告警："+logtype,content)
                        return True
            else:
                return False
        else:
            return False