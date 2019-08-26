# -*- coding: utf-8 -*-
# @Time : 2019/8/26 17:53
# @Author : wangmengmeng
from ddt import ddt,data,unpack
import unittest
from common.read_config import config
from common.send_request import request

test_data = [{"categoryCode":"sys_dictcate_shux_rule"}]

@ddt
class dictionaryDataTree(unittest.TestCase):
    """药品属性-调用的是知识建设的接口"""
    @classmethod
    def setUpClass(cls):
        cls.base_url = config.get('default','address') + '/knowledge/api/v1/dictionaryDataTree'


    @data(*test_data)
    def test_1(self,param):
        # param = {"type":1,"keyword":None}
        response = request(method='get',url = self.base_url,data = param)   # 注意调用方法时参数名为data
        self.assertEqual(response.json()['code'], '200')
        self.assertEqual(response.json()['message'], '操作成功。')