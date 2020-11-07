#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 白名单表操作
  Site: http://pirogue.org 
  Created: 2018-08-03 17:32:54
"""


from dbs.initdb import DBSession
from dbs.models.Whiteip import Whiteip
from sqlalchemy import desc,asc
from sqlalchemy.exc import InvalidRequestError

# import sys
# sys.path.append("..")

class White:
    """增删改查"""

    def __init__(self):  
        self.session=DBSession

    # 查询白名单表ip数据
    def white_ip(self):
        try:
            white_ip_res = self.session.query(Whiteip.src_host).all()
            return white_ip_res
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print (e)
        finally:
            self.session.close()
    
    # 增加白名单
    def insert_white_ip(self, src_host):
        try:
            wip_insert = Whiteip(src_host=src_host)
            self.session.merge(wip_insert)
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print (e)
        finally:
            self.session.close()