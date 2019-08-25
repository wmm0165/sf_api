# -*- coding: utf-8 -*-
# @Time : 2019/8/24 0:00
# @Author : wangmengmeng
import requests
from business.login import session
from common.read_config import config
import json

# 新建审方方案
url = "http://10.1.1.71:9999/auditcenter/api/v1/auditPlan"
plan_name = 'zhuyuan'
data = {"name": plan_name, "category": 1, "createdTime": 1566575960160, "modifiedTime": 1566575960160, "recipeSource": "0",
        "deptList": [], "groupList": [], "isOuvas": 0, "isPivas": 0, "minStay": "", "maxStay": "", "minAge": "",
        "maxAge": "", "ageUnit": "岁", "costTypes": "", "patientCondition": "", "iptWardList": [], "weekList": [],
        "startTime": "00:00", "endTime": "23:59"}
response = session.request(method='post', url=url, data=json.dumps(data), headers={'Content-Type': "application/json"})
print(response.json())
# 查询审方方案列表
url = "http://10.1.1.71:9999/auditcenter/api/v1/auditPlanList"
params = {"pageSize": 20, "page": 1}  # 可以用字典的形式传参
response = session.request("get", url=url, params=params)
print(response.url)
print(response.json())
res = response.json()
for i in range(0, (len(res['data']['recordList']) - 1)):
    if res['data']['recordList'][i]['name'] == plan_name:
        id = res['data']['recordList'][i]['id']
        print(id)
        break
# 查看方案详情
url = "http://10.1.1.71:9999/auditcenter/api/v1/auditPlan/" + str(id)
response = session.request("get", url=url, params=None)
print(response.json())
print(response.url)
# 修改方案
url = "http://10.1.1.71:9999/auditcenter/api/v1/auditPlan/" + str(id)
data = {"id": id, "name": plan_name, "category": 1, "recipeSource": 0, "minStay": None, "maxStay": None,
        "drugCategorys": None, "drugProperties": None, "isOuvas": 0, "isPivas": 0, "minAge": "1", "maxAge": None,
        "ageUnit": "岁", "costTypes": "", "diagnoses": None, "icd10": None, "userId": "-200", "userName": "系统管理员",
        "createdTime": 1566630072000, "modifiedTime": 1566630072000, "startTime": "00:00", "endTime": "23:59",
        "effectWeek": None, "deptList": [], "groupList": [], "doctorList": None, "infoList": None,
        "displayInfoList": None, "patientCondition": "", "iptWardList": [], "weekList": None}
response = session.request('put', url=url, data=json.dumps(data), headers={'Content-Type': "application/json"})
print(response.url)
print(response.json())
# 删除方案
url = "http://10.1.1.71:9999/auditcenter/api/v1/auditPlan/" + str(id)
response = session.request('delete', url=url)
print(response.json())
