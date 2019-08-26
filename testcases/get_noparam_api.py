# -*- coding: utf-8 -*-
# @Time : 2019/8/25 17:14
# @Author : wangmengmeng
import unittest
import ddt
from common.send_request import request
from common.record_log import log
from common.read_config import config

api_list = ['/api/v1/patientCondtionList',
            '/api/v1/newTaskHint',
            '/api/v1/payTypeList',
            '/api/v1/analysisType',
            '/api/v1/drugCategory',
            '/api/v1/endAuditWork'
            ]


@ddt.ddt
class GetNoParamApi(unittest.TestCase):
    """没有参数的get请求"""

    @classmethod
    def setUpClass(cls):
        log.info('------开始执行{}测试用例------'.format(cls.__doc__))

    @classmethod
    def tearDownClass(cls):
        log.info('------{}测试用例执行结束------'.format(cls.__doc__))

    @ddt.data(*api_list)
    def test_1(self, api):
        try:
            url = config.get('auditcenter', 'url') + api
            response = request(method='get', url=url)
            self.assertEqual(response.json()['code'], '200')
            self.assertEqual(response.json()['message'], 'OK')
        except AssertionError:
            print('断言失败')
            raise


if __name__ == '__main__':
    unittest.main()
