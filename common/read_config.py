# -*- coding: utf-8 -*-
# @Time : 2019/8/23 16:31
# @Author : wangmengmeng
from configparser import ConfigParser
from config.config import CONFIG_PATH
from common.record_log import log

class ReadConfig:
    def __init__(self):
        self.conf = ConfigParser()
        self.conf.read(CONFIG_PATH, encoding='utf8')

    def get(self,field,key):
        data = self.conf.get(field,key)
        if data.isdigit():
            data = int(data)
        log.info("读取配置文件{}-{}的值为{}".format(field,key,data))
        return data

config = ReadConfig()

if __name__ == '__main__':
    rc = ReadConfig()
    value = rc.get('default','address')
