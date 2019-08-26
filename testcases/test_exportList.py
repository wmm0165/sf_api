# -*- coding: utf-8 -*-
# @Time : 2019/8/26 16:22
# @Author : wangmengmeng
from ddt import ddt,data,unpack
import unittest
from common.read_config import config
from common.send_request import request

test_data = [{"exportType":5},
             {"exportType":4},
             {"exportType":1},
             {"exportType":2},
             {"exportType":6}]

@ddt
class ExportList(unittest.TestCase):
    """获取下载列表的接口"""
    @classmethod
    def setUpClass(cls):
        cls.base_url = config.get('auditcenter','url') + '/api/v1/exportList'


    @data(*test_data)
    def test_1(self,param):
        # param = {"type":1,"keyword":None}
        response = request(method='get',url = self.base_url,data = param)   # 注意调用方法时参数名为data
        self.assertEqual(response.json()['code'], '200')
        self.assertEqual(response.json()['message'], 'OK')





