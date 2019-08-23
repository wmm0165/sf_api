# -*- coding: utf-8 -*-
# @Time : 2019/8/23 16:31
# @Author : wangmengmeng
from configparser import ConfigParser
from config.config import CONFIG_PATH


class ReadConfig:
    def __init__(self):
        self.conf = ConfigParser()
        self.conf.read(CONFIG_PATH, encoding='utf8')

    def get(self,field,key):
        pass
