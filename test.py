# -*- coding: utf-8 -*-
# @Time : 2019/8/25 17:11
# @Author : wangmengmeng
import unittest
import ddt
import requests

# test_data = [{"name": "mm", "password": "e10adc3949ba59abbe56e057f20f883e", "code": "", "assert": "200"},
#              {"name": "wangmm", "password": "e10adc3949ba59abbe56e057f20f883e", "code": "", "assert": "200"}]
test_data = ['test','abd']


@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        self.url = "http://10.1.1.172:9999/syscenter/api/v1/currentUser"

    @ddt.data(*test_data)
    def test_ddt(self,value):
        # r = requests.post(self.url,value)
        # print(r.json())
        # self.assertTrue(value['assert'] in r.text)
        print(value)
if __name__ == '__main__':
    unittest.main()