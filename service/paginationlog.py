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
reload(sys)
sys.setdefaultencoding('utf8')

logselect = LogOp()


def listpage(param):
    if param.has_key("white") and param.has_key("page"):
        page = param["page"]
        # print page
        page_list = []
        second_page_list = []
        for i in logselect.page_select_white(page):
            dict_param = {"id":i.id,"dst_host":i.dst_host,"dst_port":i.dst_port,"honeycred":i.honeycred,"local_time":i.local_time.strftime("%Y-%m-%d %H:%M:%S"),"hostname":i.hostname,\
            "password":i.password,"path":i.path,"skin":i.skin,"useragent":i.useragent,"username":i.username,"session":i.session,"localversion":i.localversion,\
            "remoteversion":i.remoteversion,"df":i.df,"idid":i.idid,"inin":i.inin,"lenlen":i.lenlen,"mac":i.mac,"outout":i.outout,"prec":i.prec,\
            "proto":i.proto,"res":i.res,"syn":i.syn,"tos":i.tos,"ttl":i.ttl,"urgp":i.urgp,"window":i.window,"logtype":i.logtype,\
            "node_id":i.node_id,"src_host":i.src_host,"src_port":i.src_port}
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
                i["logtype"] = '端口扫描行为'
            elif i["logtype"] == '8001':
                i["logtype"] = 'mysql登录尝试'

            second_dict_param = {"id":i["id"],"dst_host":i["dst_host"],"dst_port":i["dst_port"],"honeycred":i["honeycred"],"local_time":i["local_time"],"hostname":i["hostname"],\
            "password":i["password"],"path":i["path"],"skin":i["skin"],"useragent":i["useragent"],"username":i["username"],"session":i["session"],"localversion":i["localversion"],\
            "remoteversion":i["remoteversion"],"df":i["df"],"idid":i["idid"],"inin":i["inin"],"lenlen":i["lenlen"],"mac":i["mac"],"outout":i["outout"],"prec":i["prec"],\
            "proto":i["proto"],"res":i["res"],"syn":i["syn"],"tos":i["tos"],"ttl":i["ttl"],"urgp":i["urgp"],"window":i["window"],"logtype":i["logtype"],\
            "node_id":i["node_id"],"src_host":i["src_host"],"src_port":i["src_port"]}

            second_page_list.append(second_dict_param)
        page_res = {"list": second_page_list}
        # print page_res
        return page_res
    else:
        if param.has_key("page"):
            page = param["page"]
            # print page
            page_list = []
            second_page_list = []
            for i in logselect.page_select_attack(page):
                dict_param = {"id":i.id,"dst_host":i.dst_host,"dst_port":i.dst_port,"honeycred":i.honeycred,"local_time":i.local_time.strftime("%Y-%m-%d %H:%M:%S"),"hostname":i.hostname,\
                "password":i.password,"path":i.path,"skin":i.skin,"useragent":i.useragent,"username":i.username,"session":i.session,"localversion":i.localversion,\
                "remoteversion":i.remoteversion,"df":i.df,"idid":i.idid,"inin":i.inin,"lenlen":i.lenlen,"mac":i.mac,"outout":i.outout,"prec":i.prec,\
                "proto":i.proto,"res":i.res,"syn":i.syn,"tos":i.tos,"ttl":i.ttl,"urgp":i.urgp,"window":i.window,"logtype":i.logtype,\
                "node_id":i.node_id,"src_host":i.src_host,"src_port":i.src_port}
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
                    i["logtype"] = '端口扫描行为'
                elif i["logtype"] == '8001':
                    i["logtype"] = 'mysql登录尝试'

                second_dict_param = {"id":i["id"],"dst_host":i["dst_host"],"dst_port":i["dst_port"],"honeycred":i["honeycred"],"local_time":i["local_time"],"hostname":i["hostname"],\
                "password":i["password"],"path":i["path"],"skin":i["skin"],"useragent":i["useragent"],"username":i["username"],"session":i["session"],"localversion":i["localversion"],\
                "remoteversion":i["remoteversion"],"df":i["df"],"idid":i["idid"],"inin":i["inin"],"lenlen":i["lenlen"],"mac":i["mac"],"outout":i["outout"],"prec":i["prec"],\
                "proto":i["proto"],"res":i["res"],"syn":i["syn"],"tos":i["tos"],"ttl":i["ttl"],"urgp":i["urgp"],"window":i["window"],"logtype":i["logtype"],\
                "node_id":i["node_id"],"src_host":i["src_host"],"src_port":i["src_port"]}

                second_page_list.append(second_dict_param)
            page_res = {"list": second_page_list}
            # print page_res
            return page_res