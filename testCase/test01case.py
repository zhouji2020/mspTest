import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
# pythoncom.CoInitialize()

url = geturlParams.geturlParams().get_url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, body, method):
        """
        set params
        :param case_name:
        :param path
        :param body
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.body = str(body)
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """

    def setUp(self):
        """

        :return:
        """
        print(self.case_name+"测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        """
        check test result
        :return:
        """

        info = RunMain().run_main(self.method, url, self.body)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为json格式
        if self.case_name == 'login':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'login_error':  # 同上
            self.assertEqual(ss['code'], -1)
        if self.case_name == 'login_null':  # 同上
            self.assertEqual(ss['code'], 10001)


