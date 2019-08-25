# -*- coding: utf-8 -*-
# @Time : 2019/8/23 15:58
# @Author : wangmengmeng
import requests
import hashlib
from common.read_config import config
import json

class Login:
    def __init__(self):
        self.session = requests.session()
        self.uername = config.get('default','username')
        password = str(config.get('default', 'password'))
        self.password = self.handle_password(password)

    def handle_password(self, password):
        m = hashlib.md5()  # 创建md5对象
        m.update(password.encode())  # 生成加密字符串
        password = m.hexdigest()
        return password

    def login(self):
        url = config.get('default','address') + '/syscenter/api/v1/currentUser'
        data = {"name": self.uername, "password": self.password}
        headers = {'Content-Type': "application/json"}
        response = self.session.post(url,data=json.dumps(data),headers=headers)

    def start_sf(self):
        url = config.get('auditcenter','url') + '/api/v1/startAuditWork'
        response = self.session.get(url)

    @property
    def get_session(self):
        self.login()
        self.start_sf()
        # print(self.session)
        return self.session

session = Login().get_session

# if __name__ == '__main__':
#     login = Login()
#     print(login.password)
#     login.login()
