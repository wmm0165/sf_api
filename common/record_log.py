# -*- coding: utf-8 -*-
# @Time : 2019/8/23 16:05
# @Author : wangmengmeng
import logging


class Record_log:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    # 将日志写进配置文件


