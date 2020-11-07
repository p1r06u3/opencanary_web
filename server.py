#!/usr/bin/env python
#coding:utf-8
"""
  Author:  pirogue --<p1r06u3@gmail.com>
  Purpose: 服务端启动文件
  Created: 2017年8月15日19:22:49
  Site:    http://pirogue.org
"""

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.autoreload
from util.task import sched, host_scheduler, check_scheduler

from application import settings
from url import url
from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)

if __name__ == '__main__':
    check_scheduler()
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=url, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port,address="127.0.0.1")
    print('Development server is running at http://127.0.0.1:%s/' % options.port)
    tornado.ioloop.IOLoop.instance().start()
    # 启动方式python server.py 或者 python server.py --port=80
