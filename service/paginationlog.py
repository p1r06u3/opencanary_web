#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 日志列表展示
  Site: http://pirogue.org 
  Created: 2018-08-06 17:25:24
"""

from dbs.dal.LogOperate import LogOp
import sys
from importlib import reload
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding('utf8')

logselect = LogOp()


def listpage(param):
    if "white" in param and "page" in param:
        page = param["page"]
        # print page
        page_list = []
        second_page_list = []
        for i in logselect.page_select_white(page):
            dict_param = {"id":i.id,"dst_host":i.dst_host,"dst_port":i.dst_port,"honeycred":i.honeycred,"local_time":i.local_time.strftime("%Y-%m-%d %H:%M:%S"),"hostname":i.hostname,\
            "password":i.password,"path":i.path,"skin":i.skin,"useragent":i.useragent,"username":i.username,"session":i.session,"localversion":i.localversion,\
            "remoteversion":i.remoteversion,"df":i.df,"idid":i.idid,"inin":i.inin,"lenlen":i.lenlen,"mac":i.mac,"outout":i.outout,"prec":i.prec,\
            "proto":i.proto,"res":i.res,"syn":i.syn,"tos":i.tos,"ttl":i.ttl,"urgp":i.urgp,"window":i.window,"logtype":i.logtype,\
            "node_id":i.node_id,"src_host":i.src_host,"src_port":i.src_port, "repo":i.repo, "ntp_cmd":i.ntp_cmd, "args":i.args, "cmd":i.cmd, "banner_id": i.banner_id,\
            "data":i.data, "function":i.function, "vnc_client_response":i.vnc_client_response, "vnc_password":i.vnc_password, "vnc_server_challenge":i.vnc_server_challenge,\
            "inputs":i.inputs, "domain":i.domain, "headers_call_id":i.headers_call_id, "headers_content_length":i.headers_content_length, "headers_cseq":i.headers_cseq,\
            "headers_from":i.headers_from, "headers_to":i.headers_to, "headers_via":i.headers_via, "community_string":i.community_string, "requests":i.requests,\
            "urg":i.urg, "psh":i.psh, "fin":i.fin, "appname":i.appname, "cltintname":i.cltintname, "database":i.database, "language":i.language, "servername":i.servername, "domainname":i.domainname}
            page_list.append(dict_param)

        for i in page_list:
            # print i
            if i["logtype"] == '2000':
                i["logtype"] = 'ftp登录尝试'
            elif i["logtype"] == '3000':
                i["logtype"] = 'web蜜罐被访问'
            elif i["logtype"] == '3001':
                i["logtype"] = 'web蜜罐被登录'
            elif i["logtype"] == '4000':
                i["logtype"] = 'ssh建立连接'
            elif i["logtype"] == '4001':
                i["logtype"] = 'ssh远程版本发送'
            elif i["logtype"] == '4002':
                i["logtype"] = 'ssh登录尝试'
            elif i["logtype"] == '6001':
                i["logtype"] = 'telnet登录尝试'
            elif i["logtype"] == '5001':
                i["logtype"] = '端口(SYN)扫描'
            elif i["logtype"] == '8001':
                i["logtype"] = 'mysql登录尝试'
            elif i["logtype"] == '16001':
                i["logtype"] = 'git clone请求'  
            elif i["logtype"] == '11001':
                i["logtype"] = 'ntp monlist请求'  
            elif i["logtype"] == '17001':
                i["logtype"] = 'redis命令'  
            elif i["logtype"] == '18001' or i["logtype"] == '18002' or i["logtype"] == '18003' or i["logtype"] == '18004' or i["logtype"] == '18005':
                i["logtype"] = 'tcp连接请求'  
            elif i["logtype"] == '12001':
                i["logtype"] = 'vnc连接'  
            elif i["logtype"] == '14001':
                i["logtype"] = 'windows远程登录'
            elif i["logtype"] == '13001':
                i["logtype"] = 'snmp扫描'
            elif i["logtype"] == '15001':
                i["logtype"] = 'sip请求'
            elif i["logtype"] == '5002':
                i["logtype"] = 'nmap os扫描'
            elif i["logtype"] == '5003':
                i["logtype"] = 'nmap null扫描'
            elif i["logtype"] == '5004':
                i["logtype"] = 'nmap xmas扫描'
            elif i["logtype"] == '5005':
                i["logtype"] = 'nmap fin扫描'
            elif i["logtype"] == '9001':
                i["logtype"] = 'mssql登录sql账户认证'
            elif i["logtype"] == '9002':
                i["logtype"] = 'mssql登录win身份认证'
            elif i["logtype"] == '7001':
                i["logtype"] = 'http代理登录尝试'

            second_dict_param = {"id":i["id"],"dst_host":i["dst_host"],"dst_port":i["dst_port"],"honeycred":i["honeycred"],"local_time":i["local_time"],"hostname":i["hostname"],\
            "password":i["password"],"path":i["path"],"skin":i["skin"],"useragent":i["useragent"],"username":i["username"],"session":i["session"],"localversion":i["localversion"],\
            "remoteversion":i["remoteversion"],"df":i["df"],"idid":i["idid"],"inin":i["inin"],"lenlen":i["lenlen"],"mac":i["mac"],"outout":i["outout"],"prec":i["prec"],\
            "proto":i["proto"],"res":i["res"],"syn":i["syn"],"tos":i["tos"],"ttl":i["ttl"],"urgp":i["urgp"],"window":i["window"],"logtype":i["logtype"],\
            "node_id":i["node_id"],"src_host":i["src_host"],"src_port":i["src_port"],"repo":i["repo"], "ntp_cmd":i["ntp_cmd"], "args":i["args"], "cmd":i["cmd"], "banner_id": i["banner_id"],\
            "data":i["data"], "function":i["function"], "vnc_client_response":i["vnc_client_response"], "vnc_password":i["vnc_password"], "vnc_server_challenge":i["vnc_server_challenge"],\
            "inputs":i["inputs"], "domain":i["domain"], "headers_call_id":i["headers_call_id"], "headers_content_length":i["headers_content_length"], "headers_cseq":i["headers_cseq"],\
            "headers_from":i["headers_from"], "headers_to":i["headers_to"], "headers_via":i["headers_via"], "community_string":i["community_string"], "requests":i["requests"],\
            "urg":i["urg"], "psh":i["psh"], "fin":i["fin"], "appname":i["appname"], "cltintname":i["cltintname"], "database":i["database"], "language":i["language"], \
            "servername":i["servername"], "domainname":i["domainname"]}

            second_page_list.append(second_dict_param)
        page_res = {"list": second_page_list}
        # print page_res
        return page_res
    else:
        if "page" in param:
            page = param["page"]
            # print page
            page_list = []
            second_page_list = []
            for i in logselect.page_select_attack(page):
                dict_param = {"id":i.id,"dst_host":i.dst_host,"dst_port":i.dst_port,"honeycred":i.honeycred,"local_time":i.local_time.strftime("%Y-%m-%d %H:%M:%S"),"hostname":i.hostname,\
            "password":i.password,"path":i.path,"skin":i.skin,"useragent":i.useragent,"username":i.username,"session":i.session,"localversion":i.localversion,\
            "remoteversion":i.remoteversion,"df":i.df,"idid":i.idid,"inin":i.inin,"lenlen":i.lenlen,"mac":i.mac,"outout":i.outout,"prec":i.prec,\
            "proto":i.proto,"res":i.res,"syn":i.syn,"tos":i.tos,"ttl":i.ttl,"urgp":i.urgp,"window":i.window,"logtype":i.logtype,\
            "node_id":i.node_id,"src_host":i.src_host,"src_port":i.src_port, "repo":i.repo, "ntp_cmd":i.ntp_cmd, "args":i.args, "cmd":i.cmd, "banner_id": i.banner_id,\
            "data":i.data, "function":i.function, "vnc_client_response":i.vnc_client_response, "vnc_password":i.vnc_password, "vnc_server_challenge":i.vnc_server_challenge,\
            "inputs":i.inputs, "domain":i.domain, "headers_call_id":i.headers_call_id, "headers_content_length":i.headers_content_length, "headers_cseq":i.headers_cseq,\
            "headers_from":i.headers_from, "headers_to":i.headers_to, "headers_via":i.headers_via, "community_string":i.community_string, "requests":i.requests,\
            "urg":i.urg, "psh":i.psh, "fin":i.fin, "appname":i.appname, "cltintname":i.cltintname, "database":i.database, "language":i.language, "servername":i.servername, "domainname":i.domainname}
                page_list.append(dict_param)

            for i in page_list:
                # print i
                if i["logtype"] == '2000':
                    i["logtype"] = 'ftp登录尝试'
                elif i["logtype"] == '3000':
                    i["logtype"] = 'web蜜罐被访问'
                elif i["logtype"] == '3001':
                    i["logtype"] = 'web蜜罐被登录'
                elif i["logtype"] == '4000':
                    i["logtype"] = 'ssh建立连接'
                elif i["logtype"] == '4001':
                    i["logtype"] = 'ssh远程版本发送'
                elif i["logtype"] == '4002':
                    i["logtype"] = 'ssh登录尝试'
                elif i["logtype"] == '6001':
                    i["logtype"] = 'telnet登录尝试'
                elif i["logtype"] == '5001':
                    i["logtype"] = '端口(SYN)扫描'
                elif i["logtype"] == '8001':
                    i["logtype"] = 'mysql登录尝试'
                elif i["logtype"] == '16001':
                    i["logtype"] = 'git clone请求'  
                elif i["logtype"] == '11001':
                    i["logtype"] = 'ntp monlist请求'  
                elif i["logtype"] == '17001':
                    i["logtype"] = 'redis命令'  
                elif i["logtype"] == '18001' or i["logtype"] == '18002' or i["logtype"] == '18003' or i["logtype"] == '18004' or i["logtype"] == '18005':
                    i["logtype"] = 'tcp连接请求'  
                elif i["logtype"] == '12001':
                    i["logtype"] = 'vnc连接'  
                elif i["logtype"] == '14001':
                    i["logtype"] = 'windows远程登录'
                elif i["logtype"] == '13001':
                    i["logtype"] = 'snmp扫描'
                elif i["logtype"] == '15001':
                    i["logtype"] = 'sip请求'
                elif i["logtype"] == '5002':
                    i["logtype"] = 'nmap os扫描'
                elif i["logtype"] == '5003':
                    i["logtype"] = 'nmap null扫描'
                elif i["logtype"] == '5004':
                    i["logtype"] = 'nmap xmas扫描'
                elif i["logtype"] == '5005':
                    i["logtype"] = 'nmap fin扫描'
                elif i["logtype"] == '9001':
                    i["logtype"] = 'mssql登录sql账户认证'
                elif i["logtype"] == '9002':
                    i["logtype"] = 'mssql登录win身份认证'
                elif i["logtype"] == '7001':
                    i["logtype"] = 'http代理登录尝试'
                    
                second_dict_param = {"id":i["id"],"dst_host":i["dst_host"],"dst_port":i["dst_port"],"honeycred":i["honeycred"],"local_time":i["local_time"],"hostname":i["hostname"],\
            "password":i["password"],"path":i["path"],"skin":i["skin"],"useragent":i["useragent"],"username":i["username"],"session":i["session"],"localversion":i["localversion"],\
            "remoteversion":i["remoteversion"],"df":i["df"],"idid":i["idid"],"inin":i["inin"],"lenlen":i["lenlen"],"mac":i["mac"],"outout":i["outout"],"prec":i["prec"],\
            "proto":i["proto"],"res":i["res"],"syn":i["syn"],"tos":i["tos"],"ttl":i["ttl"],"urgp":i["urgp"],"window":i["window"],"logtype":i["logtype"],\
            "node_id":i["node_id"],"src_host":i["src_host"],"src_port":i["src_port"],"repo":i["repo"], "ntp_cmd":i["ntp_cmd"], "args":i["args"], "cmd":i["cmd"], "banner_id": i["banner_id"],\
            "data":i["data"], "function":i["function"], "vnc_client_response":i["vnc_client_response"], "vnc_password":i["vnc_password"], "vnc_server_challenge":i["vnc_server_challenge"],\
            "inputs":i["inputs"], "domain":i["domain"], "headers_call_id":i["headers_call_id"], "headers_content_length":i["headers_content_length"], "headers_cseq":i["headers_cseq"],\
            "headers_from":i["headers_from"], "headers_to":i["headers_to"], "headers_via":i["headers_via"], "community_string":i["community_string"], "requests":i["requests"],\
            "urg":i["urg"], "psh":i["psh"], "fin":i["fin"], "appname":i["appname"], "cltintname":i["cltintname"], "database":i["database"], "language":i["language"], \
            "servername":i["servername"], "domainname":i["domainname"]}

                second_page_list.append(second_dict_param)
            page_res = {"list": second_page_list}
            # print page_res
            return page_res

def total_atk_page():
    # 查询攻击列表数量
    return logselect.select_attack_total()


def total_wit_page():
    # 查询过滤列表数量
    return logselect.select_filter_total()
