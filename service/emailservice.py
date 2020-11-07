#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 发送email
  Site: http://pirogue.org 
  Created: 2018-08-09 16:09:55
"""

import smtplib
from email.mime.text import MIMEText
from util.config import ini_info
from application import emailfile, mail_host, mail_user, mail_pass, mail_postfix
import sys
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")
else:
    from importlib import reload


def maillists():
    ini = ini_info(emailfile)
    ini.cfg_load()
    # [(u'user', u'p1r06u3@gmail.com;980555216@qq.com;a@qq.com')]
    # convert to down
    # [u'p1r06u3@gmail.com', u'980555216@qq.com', u'a@qq.com']
    return ini.cfg_dump()[0][1].split(';')


def send_mail(sub, content):
    # mailto_list=['p1r06u3@gmail.com', '980555216@qq.com']           #收件人(列表)

    # mailto_list = maillists()  #收件人(列表)
    to_list = maillists()
    me = "opencanary" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='html', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)  #将收件人列表以‘;’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)  #连接服务器
        server.login(mail_user, mail_pass)  #登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        print("email send success.")
        return True
    except Exception as e:
        print("email send failed: " + str(e))
        return False


def switches():
    ini = ini_info(emailfile)
    ini.cfg_load()
    return ini.cfg_get('email', 'switch')


def main():
    send_mail("兄弟电话1", "电话是170")  #邮件主题和邮件内容


if __name__ == '__main__':
    main()
