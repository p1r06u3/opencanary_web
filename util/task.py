#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 计划任务模块
  Site: http://pirogue.org 
  Created: 2018-02-08 11:18:10
"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from service.hostservice import hostonline
import atexit
import fcntl
#jobstores = {
#    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
#}

sched = BackgroundScheduler()

# sched.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)


def check_scheduler():
    f = open("scheduler.lock", "wb")
    sched.start()
    try:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if sched.get_job('check_host'):
            pass
        else:
            host_scheduler()
    except:
            pass
    def unlock():
        fcntl.flock(f, fcntl.LOCK_UN)
        f.close()
    atexit.register(unlock)


def host_scheduler():
    sched.add_job(hostonline, 'interval', seconds=30, id='check_host')
    print("It is \033[1;35m running \033[0m!")
    return True
