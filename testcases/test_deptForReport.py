# -*- coding: utf-8 -*-
# @Time : 2019/8/26 11:43
# @Author : wangmengmeng
from ddt import ddt,data,unpack
import unittest
from common.read_config import config
from common.send_request import request

# type = 1指门诊，type=2 指住院
test_data = [{"type":1,"keyword":None},
             {"type":2,"keyword":None},
             {"type":1,"keyword":"抗凝门诊"},
             {"type":2,"keyword":"住院的科室"},]

@ddt
class Dept(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_url = config.get('auditcenter','url') + '/api/v1/deptForReport'


    @data(*test_data)
    def test_1(self,param):
        # param = {"type":1,"keyword":None}
        response = request(method='get',url = self.base_url,data = param)   # 注意调用方法时参数名为data
        self.assertEqual(response.json()['code'], '200')
        self.assertEqual(response.json()['message'], 'OK')





