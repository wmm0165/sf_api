# -*- coding: utf-8 -*-
# @Time : 2019/8/23 16:06
# @Author : wangmengmeng
import os
from datetime import datetime


PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 项目目录
CONFIG_DIR =os.path.dirname(os.path.abspath(__file__)) # 配置文件目录
CONFIG_PATH = os.path.join(CONFIG_DIR,'config.ini')
LOG_DIR = os.path.join(PROJ_DIR,'log')
log_name = datetime.today().strftime("%Y-%m-%d") + ".log" # %Y-%m-%d-%H-%M-%S
LOG_PATH = os.path.join(LOG_DIR,log_name)  # 日志
REPORT_DIR = os.path.join(PROJ_DIR,'report')
report_name = datetime.today().strftime("%Y-%m-%d") + ".html"
REPORT_PATH = os.path.join(REPORT_DIR,report_name)  # 报告
TESTCASE_PATH = os.path.join(PROJ_DIR, 'testcases')
if __name__ == '__main__':
    print(LOG_PATH)
    print(REPORT_PATH)
    print(TESTCASE_PATH)

