import json
import unittest
import time
import paramunittest
import geturlParams
import readExcel
from common.configHttp import RunMain
from globalvar import GlobalVar

url = geturlParams.geturlParams().get_url()  # 调用geturlParams获取我们拼接的URL
authentication_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'Authentication')
# 调用readExcel中的get_xls方法获取对应表格中的内容


@paramunittest.parametrized(*authentication_xls)  # 参数化表格中的内容
class TestAuthentication(unittest.TestCase):  # 定义TestAuthentication单元测试类
    def setParameters(self, case_name, path, body, method):  # 初始化接口参数
        self.case_name = str(case_name)  # 将表格中的参数一一赋值到对应的类属性
        self.path = str(path)  # 同上
        self.body = str(body)  # 同上
        self.method = str(method)  # 同上

    def description(self):
        """
        test report description
        :return:
        """

    def setUp(self):  # 定义用例执行前进行的操作类
        """
        :return:
        """
        print(self.case_name+"测试开始前准备")  # 打印相关信息
        time.sleep(3)  # 空余3秒的时间后执行测试断言

    def tearDown(self):  # 定义用例执行后的进行的操作类
        print("测试结束，输出log完结\n\n")  # 打印相关信息

    def test_authentication(self):
        # new_url = url + '/msp/api/v1/manage/system/login'
        # body = json.dumps({"user_name": "admin", "password": "admin"})
        info_json = json.loads(RunMain().run_main(self.method, url+self.path, self.body, 'yes'))
        # 调用run_main方法来进行requests请求，并拿到json格式（即dict格式）响应
        info = RunMain().run_main(self.method, url+self.path, self.body, 'no')
        # 调用run_main方法来进行requests请求，并拿到接口原有格式响应（方便获取响应状态码及响应时间）

        if self.case_name == 'login':  # 判断case_name是login
            self.assertEqual(info_json['error'], 0)  # 判断返回中key为error的value是否为0
            self.assertEqual(info.status_code, 200)  # 判断返回的状态码是否为200
            self.assertIn('token', info.json().keys())  # 判断返回的信息中是否含有名称为‘token’的key
            token = info_json['token']  # 提取出返回中的token值
            GlobalVar().set_value('token', token)  # 调用GlobalVar中的方法将token值存入字典
        if self.case_name == 'keepalive':  # 判断case_name是keepalive
            self.assertEqual(info_json['error'], 0)  # 判断返回中key为error的value是否为0
            self.assertEqual(info.status_code, 200)  # 判断返回的状态码是否为200
        if self.case_name == 'version':  # 判断case_name是version
            self.assertEqual(info_json['error'], 0)  # 判断返回中key为error的value是否为0
            self.assertEqual(info.status_code, 200)  # 判断返回的状态码是否为200
            self.assertIn('version', info.json().keys())  # 判断返回的信息中是否含有名称为‘version’的key

# class TestSuite:


if __name__ == "__main__":  # 只运行当前模块
    '''unittest.main()  # 运行单元测试模块'''
