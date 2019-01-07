#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 解析客户端请求过来的日志
  Site: http://pirogue.org 
  Created: 2018-08-03 18:00:23
"""

from dbs.dal.LogOperate import LogOp
from service.emailservice import send_mail, switches
from service.whiteipservice import whiteips
from service.whiteportservice import whiteports
from util.task import sched
from datetime import datetime
import datetime as datetimes
import uuid

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
            # print local_time
        else:
            local_time = datetime.now()

        if jsonlog.has_key("logdata"):
            if jsonlog["logdata"].has_key("HOSTNAME"):
                hostname = jsonlog["logdata"]["HOSTNAME"]
            elif jsonlog["logdata"].has_key("HostName"):
                hostname = jsonlog["logdata"]["HostName"]
            else:
                hostname = ''

            if jsonlog["logdata"].has_key("PASSWORD"):
                password = jsonlog["logdata"]["PASSWORD"]
            elif jsonlog["logdata"].has_key("Password"):
                password = jsonlog["logdata"]["Password"]
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
            elif jsonlog["logdata"].has_key("UserName"):
                username = jsonlog["logdata"]["UserName"]
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

            # 扩表后的新加解析日志请求格式化
            if jsonlog["logdata"].has_key("REPO"):
                repo = jsonlog["logdata"]["REPO"]
            else:
                repo = ''
            
            if jsonlog["logdata"].has_key("NTP CMD"):
                ntp_cmd = jsonlog["logdata"]["NTP CMD"]
            else:
                ntp_cmd = ''

            if jsonlog["logdata"].has_key("ARGS"):
                args = jsonlog["logdata"]["ARGS"]
            else:
                args = ''

            if jsonlog["logdata"].has_key("CMD"):
                cmd = jsonlog["logdata"]["CMD"]
            else:
                cmd = ''

            if jsonlog["logdata"].has_key("BANNER_ID"):
                banner_id = jsonlog["logdata"]["BANNER_ID"]
            else:
                banner_id = ''

            if jsonlog["logdata"].has_key("DATA"):
                data = jsonlog["logdata"]["DATA"]
            else:
                data = ''      

            if jsonlog["logdata"].has_key("FUNCTION"):
                function = jsonlog["logdata"]["FUNCTION"]
            else:
                function = ''           

            if jsonlog["logdata"].has_key("VNC Client Response"):
                vnc_client_response = jsonlog["logdata"]["VNC Client Response"]
            else:
                vnc_client_response = '' 

            if jsonlog["logdata"].has_key("VNC Password"):
                vnc_password = jsonlog["logdata"]["VNC Password"]
            else:
                vnc_password = '' 

            if jsonlog["logdata"].has_key("VNC Server Challenge"):
                vnc_server_challenge = jsonlog["logdata"]["VNC Server Challenge"]
            else:
                vnc_server_challenge = '' 

            if jsonlog["logdata"].has_key("INPUT"):
                inputs = jsonlog["logdata"]["INPUT"]
            else:
                inputs = '' 

            if jsonlog["logdata"].has_key("DOMAIN"):
                domain = jsonlog["logdata"]["DOMAIN"]
            else:
                domain = '' 

            if jsonlog["logdata"].has_key("HEADERS"):
                if jsonlog["logdata"]["HEADERS"].has_key("call-id"):
                    headers_call_id = jsonlog["logdata"]["HEADERS"]["call-id"][0]
                else:
                    headers_call_id = ''

                if jsonlog["logdata"]["HEADERS"].has_key("content_length"):
                    headers_content_length = jsonlog["logdata"]["HEADERS"]["content_length"][0]
                else:
                    headers_content_length = ''

                if jsonlog["logdata"]["HEADERS"].has_key("cseq"):
                    headers_cseq = jsonlog["logdata"]["HEADERS"]["cseq"][0]
                else:
                    headers_cseq = ''

                if jsonlog["logdata"]["HEADERS"].has_key("from"):
                    headers_from = jsonlog["logdata"]["HEADERS"]["from"][0]
                else:
                    headers_from = ''

                if jsonlog["logdata"]["HEADERS"].has_key("to"):
                    headers_to = jsonlog["logdata"]["HEADERS"]["to"][0]
                else:
                    headers_to = ''

                if jsonlog["logdata"]["HEADERS"].has_key("via"):
                    headers_via = jsonlog["logdata"]["HEADERS"]["via"][0]
                else:
                    headers_via = ''
            else:
                headers_call_id = ''
                headers_content_length = ''
                headers_cseq = ''
                headers_from = ''
                headers_to = ''
                headers_via = ''

            if jsonlog["logdata"].has_key("COMMUNITY_STRING"):
                community_string = jsonlog["logdata"]["COMMUNITY_STRING"]
            else:
                community_string = '' 

            if jsonlog["logdata"].has_key("REQUESTS"):
                requests = jsonlog["logdata"]["REQUESTS"][0]
            else:
                requests = '' 

            if jsonlog["logdata"].has_key("URG"):
                urg = jsonlog["logdata"]["URG"]
            else:
                urg = ''

            if jsonlog["logdata"].has_key("PSH"):
                psh = jsonlog["logdata"]["PSH"]
            else:
                psh = '' 

            if jsonlog["logdata"].has_key("FIN"):
                fin = jsonlog["logdata"]["FIN"]
            else:
                fin = ''

            if jsonlog["logdata"].has_key("AppName"):
                appname = jsonlog["logdata"]["AppName"]
            else:
                appname = ''

            if jsonlog["logdata"].has_key("CltIntName"):
                cltintname = jsonlog["logdata"]["CltIntName"]
            else:
                cltintname = ''

            if jsonlog["logdata"].has_key("Database"):
                database = jsonlog["logdata"]["Database"]
            else:
                database = ''

            if jsonlog["logdata"].has_key("Language"):
                language = jsonlog["logdata"]["Language"]
            else:
                language = ''

            if jsonlog["logdata"].has_key("ServerName"):
                servername = jsonlog["logdata"]["ServerName"]
            else:
                servername = ''

            if jsonlog["logdata"].has_key("DOMAINNAME"):
                domainname = jsonlog["logdata"]["DOMAINNAME"]
            else:
                domainname = ''

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
            # 二次开发日志格式增加字段
            repo = ''
            ntp_cmd = ''
            args = ''
            cmd = ''
            banner_id = ''
            data = ''
            function = ''
            vnc_client_response = ''
            vnc_password = ''
            vnc_server_challenge = ''
            inputs = ''
            domain = ''

            community_string = ''
            requests = ''
            urg = ''
            psh = ''
            fin = ''

            appname = ''
            cltintname = ''
            database = ''
            language = ''
            servername = ''
            domainname = ''

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
                # 判断目的端口是否存在于白名单端口中
                if int(dst_port) in whiteports():
                    return True
                # 判断目的ip等于来源ip
                elif dst_host == src_host:
                    return True
                else:
                    # 将客户端post过来的数据插入数据库
                    logbool = loginst.insert(dst_host, dst_port, honeycred, local_time, hostname, password, path, skin,\
                        useragent, username, session, localversion, remoteversion, df, idid, inin, lenlen, mac, outout,\
                        prec, proto, res, syn, tos, ttl, urgp, window, logtype, node_id, src_host, src_port, white,\
                        # 扩表新增
                        repo, ntp_cmd, args, cmd, banner_id, data, function, vnc_client_response, vnc_password, \
                        vnc_server_challenge, inputs, domain, headers_call_id, headers_content_length,headers_cseq, \
                        headers_from, headers_to, headers_via, community_string, requests, urg, psh, fin, \
                        appname, cltintname, database, language, servername, domainname)

                    if logbool and white == 2:
                        # 发送邮件功能
                        if switches() == 'on':
                            if str(logtype) == '2000':
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
                                logtype = '端口(SYN)扫描'
                            elif str(logtype) == '8001':
                                logtype = 'mysql登录尝试'
                            # 扩表新增
                            elif str(logtype) == '9418':
                                logtype = 'git clone请求'
                            elif str(logtype) == '11001':
                                logtype = 'ntp monlist请求'
                            elif str(logtype) == '17001':
                                logtype = 'redis命令'
                            elif (str(logtype) == '18001' or str(logtype) == '18002' or \
                            str(logtype) == '18003' or str(logtype) == '18004' or str(logtype) == '18005'):
                                logtype = 'TCP连接请求'
                            elif str(logtype) == '12001':
                                logtype = 'vnc连接'
                            elif str(logtype) == '14001':
                                logtype = 'windows远程登录'
                            elif str(logtype) == '13001':
                                logtype = 'snmp扫描'
                            elif str(logtype) == '15001':
                                logtype = 'sip请求'
                            elif str(logtype) == '5002':
                                logtype = 'NMAP OS扫描'
                            elif str(logtype) == '5003':
                                logtype = 'NMAP NULL扫描'
                            elif str(logtype) == '5004':
                                logtype = 'NMAP XMAS扫描'
                            elif str(logtype) == '5005':
                                logtype = 'NMAP FIN扫描'
                            elif str(logtype) == '9001':
                                logtype = 'mssql登录sql账户认证'
                            elif str(logtype) == '9002':
                                logtype = 'mssql登录win身份认证'
                            elif str(logtype) == '7001':
                                logtype = 'http代理登录尝试'
                            content = "攻击主机：" + src_host + "--" + "被攻击主机：" + dst_host + "--" + "攻击时间：" + local_time
                            # 将发送邮件丢到任务队列
                            sched.add_job(
                                send_mail,
                                'date',
                                run_date=(datetime.now() +
                                          datetimes.timedelta(seconds=1)),
                                args=["蜜罐告警：" + logtype, content],
                                id=str(uuid.uuid1()))
                            # send_mail("蜜罐告警："+logtype,content)
                            return True
            else:
                return False
        else:
            return False