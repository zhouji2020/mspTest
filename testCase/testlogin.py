import json
import unittest
import time
import paramunittest
import geturlParams
import readExcel
from common.configHttp import RunMain

url = geturlParams.geturlParams().get_url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'Authentication')


@paramunittest.parametrized(*login_xls)
class TestAuthentication(unittest.TestCase):
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

    def test_login(self):
        # new_url = url + '/msp/api/v1/manage/system/login'
        # body = json.dumps({"user_name": "admin", "password": "admin"})
        info = json.loads(RunMain().run_main(self.method, url+self.path, self.body))  # 调用run_main方法来进行requests请求，并拿到响应
        time.sleep(3)
        if self.case_name == 'login':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(info['error'], 0)
        if self.case_name == 'keepalive':  # 同上
            self.assertEqual(info['error'], 0)
        if self.case_name == 'version':  # 同上
            self.assertEqual(info['error'], 0)

# class TestSuite:


if __name__ == "__main__":
    unittest.main()
