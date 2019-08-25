import unittest
from common.HTMLTestReportCN import HTMLTestRunner
from config.config import REPORT_PATH
from config.config import TESTCASE_PATH


suite = unittest.defaultTestLoader.discover(TESTCASE_PATH)
with open(REPORT_PATH, 'wb') as f:  # 从配置文件中读取
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="wangmengmeng").run(suite)
