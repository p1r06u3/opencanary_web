#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 邮件、白名单配置
  Site: http://pirogue.org 
  Created: 2018-08-08 14:59:54
"""

import configparser
import sys
sys.path.append("..")
from application import emailfile


class ini_info(object):
    def __init__(self, recordfile):
        self.logfile = recordfile
        self.cfg = configparser.ConfigParser()

    def cfg_load(self):
        self.cfg.read(self.logfile)

    def cfg_dump(self):
        se_list = self.cfg.sections()
        # print('='*30)
        for se in se_list:
            # print 'a'
            # print(se)
            # print 'b'
            # print(self.cfg.items(se))
            # self.cfg.items(se)
            # print('='*30)
            return self.cfg.items(se)

    def cfg_get(self, section, option):
        v = self.cfg.get(section, option)
        print(v)
        return v

    def delete_item(self, section, key):
        self.cfg.remove_option(section, key)

    def delte_section(self, section):
        self.cfg.remove_section(section)

    def add_section(self, section):
        self.cfg.add_section(section)

    def set_item(self, section, key, value):
        self.cfg.set(section, key, value)

    def save(self):
        fp = open(self.logfile, 'w')
        self.cfg.write(fp)
        fp.close()


if __name__ == '__main__':
    ini = ini_info(emailfile)
    ini.cfg_load()
    ini.cfg_dump()

    ini.set_item('email', 'user', 'quyifei@meituan.com;980555216@qq.com')
    ini.cfg_dump()
    ini.cfg_get('email', 'switch')

    # ini.add_section('rose')
    # ini.set_item('rose', 'pwd', 'ccc')
    # ini.set_item('rose', 'port', '8080')
    # ini.cfg_dump()

    # ini.delte_section('tom')
    # ini.cfg_dump()

    ini.save()
