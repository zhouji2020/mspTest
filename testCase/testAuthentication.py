import json
import unittest
import time
import paramunittest
import geturlParams
import readExcel
from common.configHttp import RunMain
from globalvar import GlobalVar

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

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test_login(self):
        # new_url = url + '/msp/api/v1/manage/system/login'
        # body = json.dumps({"user_name": "admin", "password": "admin"})
        info_json = json.loads(RunMain().run_main(self.method, url+self.path, self.body, 'yes'))
        # 调用run_main方法来进行requests请求，并拿到json格式（即dict格式）响应
        info = RunMain().run_main(self.method, url+self.path, self.body, 'no')
        # 调用run_main方法来进行requests请求，并拿到接口原有格式响应（方便获取响应状态码及响应时间）
        time.sleep(3)
        if self.case_name == 'login':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(info_json['error'], 0)  #
            self.assertEqual(info.status_code, 200)
            self.assertIn('token', info.json().keys())
            token = info_json['token']
            GlobalVar.set_value('token', token)
        if self.case_name == 'keepalive':  # 同上
            self.assertEqual(info_json['error'], 0)
            self.assertEqual(info.status_code, 200)
        if self.case_name == 'version':  # 同上
            self.assertEqual(info_json['error'], 0)
            self.assertEqual(info.status_code, 200)
            self.assertIn('version', info.json().keys())

# class TestSuite:


if __name__ == "__main__":
    unittest.main()
