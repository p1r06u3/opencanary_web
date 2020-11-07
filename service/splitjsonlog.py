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
        if "dst_host" in jsonlog:
            dst_host = jsonlog["dst_host"]
            # print type(dst_host)
        else:
            dst_host = ''

        if "dst_port" in jsonlog:
            dst_port = jsonlog["dst_port"]
        else:
            dst_port = 0

        if "honeycred" in jsonlog:
            honeycred = jsonlog["honeycred"]
        else:
            honeycred = False

        if "local_time" in jsonlog:
            local_time = jsonlog["local_time"]
            # print local_time
        else:
            local_time = datetime.now()

        if "logdata" in jsonlog:
            if "HOSTNAME" in jsonlog["logdata"]:
                hostname = jsonlog["logdata"]["HOSTNAME"]
            elif "HostName" in jsonlog["logdata"]:
                hostname = jsonlog["logdata"]["HostName"]
            else:
                hostname = ''

            if "PASSWORD" in jsonlog["logdata"]:
                password = jsonlog["logdata"]["PASSWORD"]
            elif "Password" in jsonlog["logdata"]:
                password = jsonlog["logdata"]["Password"]
            else:
                password = ''

            if "PATH" in jsonlog["logdata"]:
                path = jsonlog["logdata"]["PATH"]
            else:
                path = ''

            if "SKIN" in jsonlog["logdata"]:
                skin = jsonlog["logdata"]["SKIN"]
            else:
                skin = ''

            if "USERAGENT" in jsonlog["logdata"]:
                useragent = jsonlog["logdata"]["USERAGENT"]
            else:
                useragent = ''

            if "USERNAME" in jsonlog["logdata"]:
                username = jsonlog["logdata"]["USERNAME"]
            elif "UserName" in jsonlog["logdata"]:
                username = jsonlog["logdata"]["UserName"]
            else:
                username = ''

            if "SESSION" in jsonlog["logdata"]:
                session = jsonlog["logdata"]["SESSION"]
            else:
                session = ''

            if "LOCALVERSION" in jsonlog["logdata"]:
                localversion = jsonlog["logdata"]["LOCALVERSION"]
            else:
                localversion = ''

            if "REMOTEVERSION" in jsonlog["logdata"]:
                remoteversion = jsonlog["logdata"]["REMOTEVERSION"]
            else:
                remoteversion = ''

            if "DF" in jsonlog["logdata"]:
                df = jsonlog["logdata"]["DF"]
            else:
                df = ''

            if "ID" in jsonlog["logdata"]:
                idid = jsonlog["logdata"]["ID"]
            else:
                idid = ''

            if "IN" in jsonlog["logdata"]:
                inin = jsonlog["logdata"]["IN"]
            else:
                inin = ''

            if "LEN" in jsonlog["logdata"]:
                lenlen = jsonlog["logdata"]["LEN"]
            else:
                lenlen = ''

            if "MAC" in jsonlog["logdata"]:
                mac = jsonlog["logdata"]["MAC"]
            else:
                mac = ''

            if "OUT" in jsonlog["logdata"]:
                outout = jsonlog["logdata"]["OUT"]
            else:
                outout = ''

            if "PREC" in jsonlog["logdata"]:
                prec = jsonlog["logdata"]["PREC"]
            else:
                prec = ''

            if "PROTO" in jsonlog["logdata"]:
                proto = jsonlog["logdata"]["PROTO"]
            else:
                proto = ''

            if "RES" in jsonlog["logdata"]:
                res = jsonlog["logdata"]["RES"]
            else:
                res = ''

            if "SYN" in jsonlog["logdata"]:
                syn = jsonlog["logdata"]["SYN"]
            else:
                syn = ''

            if "TOS" in jsonlog["logdata"]:
                tos = jsonlog["logdata"]["TOS"]
            else:
                tos = ''

            if "TTL" in jsonlog["logdata"]:
                ttl = jsonlog["logdata"]["TTL"]
            else:
                ttl = ''

            if "URGP" in jsonlog["logdata"]:
                urgp = jsonlog["logdata"]["URGP"]
            else:
                urgp = ''

            if "WINDOW" in jsonlog["logdata"]:
                window = jsonlog["logdata"]["WINDOW"]
            else:
                window = ''

            # 扩表后的新加解析日志请求格式化
            if "REPO" in jsonlog["logdata"]:
                repo = jsonlog["logdata"]["REPO"]
            else:
                repo = ''
            
            if "NTP CMD" in jsonlog["logdata"]:
                ntp_cmd = jsonlog["logdata"]["NTP CMD"]
            else:
                ntp_cmd = ''

            if "ARGS" in jsonlog["logdata"]:
                args = jsonlog["logdata"]["ARGS"]
            else:
                args = ''

            if "CMD" in jsonlog["logdata"]:
                cmd = jsonlog["logdata"]["CMD"]
            else:
                cmd = ''

            if "BANNER_ID" in jsonlog["logdata"]:
                banner_id = jsonlog["logdata"]["BANNER_ID"]
            else:
                banner_id = ''

            if "DATA" in jsonlog["logdata"]:
                data = jsonlog["logdata"]["DATA"]
            else:
                data = ''      

            if "FUNCTION" in jsonlog["logdata"]:
                function = jsonlog["logdata"]["FUNCTION"]
            else:
                function = ''           

            if "VNC Client Response" in jsonlog["logdata"]:
                vnc_client_response = jsonlog["logdata"]["VNC Client Response"]
            else:
                vnc_client_response = '' 

            if "VNC Password" in jsonlog["logdata"]:
                vnc_password = jsonlog["logdata"]["VNC Password"]
            else:
                vnc_password = '' 

            if "VNC Server Challenge" in jsonlog["logdata"]:
                vnc_server_challenge = jsonlog["logdata"]["VNC Server Challenge"]
            else:
                vnc_server_challenge = '' 

            if "INPUT" in jsonlog["logdata"]:
                inputs = jsonlog["logdata"]["INPUT"]
            else:
                inputs = '' 

            if "DOMAIN" in jsonlog["logdata"]:
                domain = jsonlog["logdata"]["DOMAIN"]
            else:
                domain = '' 

            if "HEADERS" in jsonlog["logdata"]:
                if "call-id" in jsonlog["logdata"]["HEADERS"]:
                    headers_call_id = jsonlog["logdata"]["HEADERS"]["call-id"][0]
                else:
                    headers_call_id = ''

                if "content_length" in jsonlog["logdata"]["HEADERS"]:
                    headers_content_length = jsonlog["logdata"]["HEADERS"]["content_length"][0]
                else:
                    headers_content_length = ''

                if "cseq" in jsonlog["logdata"]["HEADERS"]:
                    headers_cseq = jsonlog["logdata"]["HEADERS"]["cseq"][0]
                else:
                    headers_cseq = ''

                if "from" in jsonlog["logdata"]["HEADERS"]:
                    headers_from = jsonlog["logdata"]["HEADERS"]["from"][0]
                else:
                    headers_from = ''

                if "to" in jsonlog["logdata"]["HEADERS"]:
                    headers_to = jsonlog["logdata"]["HEADERS"]["to"][0]
                else:
                    headers_to = ''

                if "via" in jsonlog["logdata"]["HEADERS"]:
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

            if "COMMUNITY_STRING" in jsonlog["logdata"]:
                community_string = jsonlog["logdata"]["COMMUNITY_STRING"]
            else:
                community_string = '' 

            if "REQUESTS" in jsonlog["logdata"]:
                requests = jsonlog["logdata"]["REQUESTS"][0]
            else:
                requests = '' 

            if "URG" in jsonlog["logdata"]:
                urg = jsonlog["logdata"]["URG"]
            else:
                urg = ''

            if "PSH" in jsonlog["logdata"]:
                psh = jsonlog["logdata"]["PSH"]
            else:
                psh = '' 

            if "FIN" in jsonlog["logdata"]:
                fin = jsonlog["logdata"]["FIN"]
            else:
                fin = ''

            if "AppName" in jsonlog["logdata"]:
                appname = jsonlog["logdata"]["AppName"]
            else:
                appname = ''

            if "CltIntName" in jsonlog["logdata"]:
                cltintname = jsonlog["logdata"]["CltIntName"]
            else:
                cltintname = ''

            if "Database" in jsonlog["logdata"]:
                database = jsonlog["logdata"]["Database"]
            else:
                database = ''

            if "Language" in jsonlog["logdata"]:
                language = jsonlog["logdata"]["Language"]
            else:
                language = ''

            if "ServerName" in jsonlog["logdata"]:
                servername = jsonlog["logdata"]["ServerName"]
            else:
                servername = ''

            if "DOMAINNAME" in jsonlog["logdata"]:
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

        if "logtype" in jsonlog:
            logtype = jsonlog["logtype"]
        else:
            logtype = ''

        if "node_id" in jsonlog:
            node_id = jsonlog["node_id"]
        else:
            node_id = ''

        if "src_host" in jsonlog:
            src_host = jsonlog["src_host"]
        else:
            src_host = ''

        if "src_port" in jsonlog:
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
