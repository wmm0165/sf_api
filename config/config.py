# -*- coding: utf-8 -*-
# @Time : 2019/8/23 16:06
# @Author : wangmengmeng
import os


PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 项目目录
CONFIG_DIR =os.path.dirname(os.path.abspath(__file__)) # 配置文件目录
CONFIG_PATH = os.path.join(CONFIG_DIR,'config.ini')
LOG_DIR = os.path.join(PROJ_DIR,'log')


if __name__ == '__main__':
    print(LOG_DIR)

