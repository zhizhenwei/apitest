# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 14:56
# @Author  : Evan.zhi
# @File    : test_case.py
# @Software: PyCharm


import pytest,os,allure
from common.utils import Utils
from common.handle_path import CASE_DIR
from common.handle_requests import HandleRequest

datas = Utils.handle_yaml(os.path.join(CASE_DIR,'case_data.yaml'))


class TestCase(Utils):

    @pytest.mark.send_code
    @allure.title("{data[title]}")
    @pytest.mark.parametrize('data',datas['send_code'])
    def test_send_code(self,data):
        res = HandleRequest().send_request(**data['account'])
        assert self.assert_resp(res.json(),data['expected'])

    @pytest.mark.login
    @allure.title("{data[title]}")
    @pytest.mark.parametrize('data',datas['login'])
    def test_login(self,data):
        res = HandleRequest().send_request(**data['account'])
        self.extract(res.json(),data['extract'])
        assert self.assert_resp(res.json(), data['expected'])



