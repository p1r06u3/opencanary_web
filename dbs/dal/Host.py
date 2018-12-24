#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 主机表操作
  Site: http://pirogue.org 
  Created: 2018-10-31 10:29:04
"""

from dbs.initdb import DBSession
from dbs.models.Host import Host
from sqlalchemy import desc, asc, extract, func, distinct
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.dialects.mysql import insert


class HostOp:
    """增删改查"""

    def __init__(self):
        self.session = DBSession

    def insert_data(self, id, last_time, hostname, ip, status):
        insert_stmt = insert(Host). \
        values(id=id, last_time=last_time, hostname=hostname, ip=ip, status=status)

        on_conflict_stmt = insert_stmt.on_duplicate_key_update(
            last_time=last_time, status=status)
        try:
            self.session.execute(on_conflict_stmt)
            self.session.commit()
            return True
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    def select_data(self):
        """查询在线主机"""
        try:
            host_online = self.session.query(Host).filter(
                Host.status == "online").order_by(desc(Host.last_time)).all()
            # print host_online
            return host_online
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    def select_allhost(self):
        """查询在线主机"""
        try:
            all_host = self.session.query(Host).order_by(desc(Host.last_time)).all()
            # print all_host
            return all_host
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()