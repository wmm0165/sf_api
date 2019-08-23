# -*- coding: utf-8 -*-
# @Time : 2019/8/23 15:58
# @Author : wangmengmeng
import requests
import hashlib
# from common.read_config import ReadConfig


class Login:
    def __init__(self):
        # self.conf = ReadConfig()
        password = '123456'
        self.password = self.handle_password(password)

    def handle_password(self, password):
        m = hashlib.md5()  # 创建md5对象
        m.update(password.encode())  # 生成加密字符串
        password = m.hexdigest()
        return password


if __name__ == '__main__':
    login = Login()
    print(login.password)