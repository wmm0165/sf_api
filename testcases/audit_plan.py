# -*- coding: utf-8 -*-
# @Time : 2019/8/24 23:09
# @Author : wangmengmeng
import unittest
from common.read_config import config
from common.send_request import request
from common.record_log import log
import sys


class AuditPlanTest(unittest.TestCase):
    """审方方案接口"""

    @classmethod
    def setUpClass(cls):
        log.info('------开始执行{}测试用例------'.format(cls.__doc__))
        cls.g = globals()
        cls.base_url = config.get('auditcenter', 'url') + '/api/v1/auditPlan'
        cls.plan_list = config.get('auditcenter', 'url') + '/api/v1/auditPlanList'
        cls.plan_name = "测试审方方案"

    @classmethod
    def tearDownClass(cls):
        log.info('------{}测试用例执行结束------'.format(cls.__doc__))

    def test_1_add_auditplan(self):
        """添加审方方案"""
        data = {"name": self.plan_name, "category": 1, "createdTime": 1566575960160, "modifiedTime": 1566575960160,
                "recipeSource": "0",
                "deptList": [], "groupList": [], "isOuvas": 0, "isPivas": 0, "minStay": "", "maxStay": "", "minAge": "",
                "maxAge": "", "ageUnit": "岁", "costTypes": "", "patientCondition": "", "iptWardList": [],
                "weekList": [],
                "startTime": "00:00", "endTime": "23:59"}
        response = request(method='post', url=self.base_url, data=data)
        self.assertEqual(response.json()['code'], '200')
        self.assertEqual(response.json()['message'], 'OK')

    def test_2_query_planlist(self):
        """查询审方方案列表"""
        params = {"pageSize": 20, "page": 1}
        response = request(method='get', url=self.plan_list, params=params)
        res = response.json()
        id = 0
        for i in range(0, (len(res['data']['recordList']) - 1)):
            if res['data']['recordList'][i]['name'] == self.plan_name:
                id = res['data']['recordList'][i]['id']
                # print(id)
                break
        self.g['a'] = id
        print(self.g['a'])
        self.assertEqual(response.json()['code'], '200')
        self.assertEqual(response.json()['message'], 'OK')

    def test_3_plandetail(self):
        # """查看审方方案详情"""
        url = self.base_url + '/' + str(self.g['a'])
        response = request(method='get', url=url)
        self.assertEqual(response.json()['code'], '200')
        self.assertEqual(response.json()['message'], 'OK')
        print(response.json())

    def test_4_alert_auditplan(self):
        """修改审方方案"""
        url = self.base_url + '/' + str(self.g['a'])
        data = {"id": self.g['a'], "name": self.plan_name, "category": 1, "recipeSource": 0, "minStay": None,
                "maxStay": None,
                "drugCategorys": None, "drugProperties": None, "isOuvas": 0, "isPivas": 0, "minAge": "1",
                "maxAge": None,
                "ageUnit": "岁", "costTypes": "", "diagnoses": None, "icd10": None, "userId": "-200",
                "userName": "系统管理员",
                "createdTime": 1566630072000, "modifiedTime": 1566630072000, "startTime": "00:00", "endTime": "23:59",
                "effectWeek": None, "deptList": [], "groupList": [], "doctorList": None, "infoList": None,
                "displayInfoList": None, "patientCondition": "", "iptWardList": [], "weekList": None}
        response = request(method='put', url=url, data=data)
        self.assertEqual(response.json()['code'],'200')
        self.assertEqual(response.json()['message'], 'OK')
        print(response.json())

    def test_5_del_auditplan(self):
        """删除审方方案"""
        url = self.base_url + '/' + str(self.g['a'])
        response = request(method='delete', url=url)
        self.assertEqual(response.json()['code'], '200')
        self.assertEqual(response.json()['message'], 'OK')
        print(response.json())


if __name__ == '__main__':
    unittest.main()
