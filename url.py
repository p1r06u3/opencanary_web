#!/usr/bin/env python
#coding:utf-8
"""
  Author:  pirogue --<p1r06u3@gmail.com>
  Purpose: URL路由配置文件
  Created: 2017/4/8
  Site:    http://pirogue.org
"""

from handlers import login
from handlers import logcollection, paginationlog, login, hello, email, index, chart, whiteiplist
import unittest


url = [
    # LoginHandler url
    (r"/", index.IndexHandler),
    (r"/auth/*", login.AuthHandler),
    (r"/log/*", logcollection.ReceiveJsonHandler),
    (r"/log/list/*", paginationlog.GetlistJsonHandler),
    (r"/mail/*", email.EmailModifyHandler),
    (r"/chart/*", chart.ChartHandler),
    (r"/whiteiplist/", whiteiplist.WhiteiplistHandler),
    (r".*", index.IndexHandler)

    # (r"/logout", login.LogoutHandler),
]



if __name__ == '__main__':
    unittest.main()