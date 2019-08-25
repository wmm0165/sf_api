# -*- coding: utf-8 -*-
# @Time : 2019/8/23 16:05
# @Author : wangmengmeng
import logging
from config.config import LOG_PATH
class Record_log:
    def __init__(self,name=__name__):
        self.logger = logging.getLogger(name)
        self.format = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        self.logger.setLevel(logging.DEBUG)

    def get_filehandler(self,filename):
        """日志写进文件"""
        fh = logging.FileHandler(filename=filename,mode='w',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.format)
        self.logger.addHandler(fh)


    def get_streamhandler(self):
        """日志打印到控制台"""
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.format)
        self.logger.addHandler(sh)

    @property
    def get_log(self):
        self.get_filehandler(LOG_PATH)
        self.get_streamhandler()
        return self.logger

log = Record_log().get_log
# log.info("测试日志")





