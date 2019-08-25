# -*- coding: utf-8 -*-
# @Time : 2019/8/23 17:16
# @Author : wangmengmeng
import requests
from business.login import session
import json
from common.record_log import log

class SendRequest:
    def __init__(self):
        pass

    def send_request(self, method, url, data=None, **kwargs):
        if method == 'post':
            response = session.request(method=method, url=url, data=json.dumps(data),
                                       headers={'Content-Type': "application/json"})
            log.info("开始发送{}请求，URL为：{}，请求数据为:{}".format(method, url, data))
        elif method == 'get':
            response = session.request(method=method, url=url, params=data)
            log.info("开始发送{}请求，URL为：{}，请求数据为:{}".format(method, url, data))
        elif method == 'put':
            response = session.request(method=method, url=url, data=json.dumps(data),
                                       headers={'Content-Type': "application/json"})
            log.info("开始发送{}请求，URL为：{}，请求数据为:{}".format(method, url, data))
        elif method == 'delete':
            response = session.request(method=method, url=url, params=data)
            log.info("开始发送{}请求，URL为：{}，请求数据为:{}".format(method, url, data))
        else:
            print("请求方法错误...")
        return response

    def __call__(self, method, url, data=None, **kwargs):
        return self.send_request(method=method, url=url, data=data, **kwargs)


request = SendRequest()  # request可以直接调用__call__


