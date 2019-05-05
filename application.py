#!/usr/bin/env python
#coding:utf-8
"""
  Author:  pirogue --<p1r06u3@gmail.com>
  Purpose: 应用配置文件
  Created: 2017/4/8
  Site:    http://pirogue.org
"""

import os
import logging
from base64 import b64encode
from uuid import uuid4


settings = dict(
    # 设置Debug开关
    debug=True,
    # 设置templates路径
    template_path=os.path.join(os.path.dirname(__file__), "dist"),
    # 设置静态文件解析路径
    static_path=os.path.join(os.path.dirname(__file__), "dist/static"),
    # 设置cookie密钥
    cookie_secret=b64encode(uuid4().bytes + uuid4().bytes),
    login_url="/login",
)

# 收件人配置列表
emailfile = os.path.join(os.path.dirname(__file__), "util/conf", "email.ini")
# smtp邮件服务器配置
mail_host = "smtp.163.com"  #使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user = "qyfllyj"  #用户名
mail_pass = "opencanary123"  #密码
mail_postfix = "163.com"  #邮箱的后缀，网易就是163.com

# web日志配置
logfile = os.path.join(os.path.dirname(__file__), "logs", "app.log")
handler = logging.FileHandler(logfile)
logger = logging.getLogger()

logger.addHandler(handler)
logger.setLevel(logging.NOTSET)
