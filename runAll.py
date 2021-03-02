import datetime
import os
# import common.HTMLTestRunner as HTMLTestRunner
import sys
import time
import getpathInfo
import unittest
import readConfig
from common.configEmail import SendMail
from apscheduler.schedulers.blocking import BlockingScheduler
import pythoncom
import common.Log
from BeautifulReport import BeautifulReport

path = getpathInfo.get_path()
result_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')
log = common.Log.logger
log_path = os.path.join(result_path, 'logs')  # 存放log文件的路径
sys.stdout = open(log_path, mode='w', encoding='utf-8')


class AllTest:  # 定义一个类AllTest
    def __init__(self):  # 初始化一些参数和数据
        '''global reportPath
        reportPath = os.path.join(result_path, "report.html")  # result/report.html'''
        self.caseListFile = os.path.join(path, "caselist.txt")  # 配置执行哪些测试文件的配置文件路径
        self.caseFile = os.path.join(path, "testCase")  # 真正的测试断言文件路径
        self.caseList = []
        log.info('测试结果路径为:' + result_path)  # 将resultPath的值输入到日志，方便定位查看问题
        log.info('测试用例列表路径'+self.caseListFile)  # 同理

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))  # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close()

    def set_case_suite(self):
        """

        :return:
        """
        self.set_case_list()  # 通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:  # 从caselist元素组中循环取出case
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            # print(case_name+".py")  # 打印出取出来的名称
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            suite_module.append(discover)  # 将discover存入suite_module元素组
            # print('suite_module:'+str(suite_module))
        if len(suite_module) > 0:  # 判断suite_module元素组是否存在元素
            for suite in suite_module:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite  # 返回测试集

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()  # 调用set_case_suite获取test_suite
            print('实际执行测试用例列表为：' + str(self.caseList))
            log.info('实际执行测试用例列表为：' + str(self.caseList))  # 同理
            print("*********TEST START*********")
            log.info("*********TEST START*********")
            # print(str(suit))
            if suit is not None:  # 判断test_suite是否为空
                # print('if-suit')
                # fp = open(reportPath, 'wb')  # 打开result/report.html测试报告文件，如果不存在就创建
                # 调用HTMLTestRunner
                # now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
                filename = '测试报告'
                runner = BeautifulReport(suit).report(description='测试报告', filename=filename, report_dir=result_path)
                runner.run(suit)
            else:
                print("Have no case to test.")
                log.info("Have no case to test.")
        except Exception as ex:
            print(str(ex))
            # log.info(str(ex))

        finally:
            print("*********TEST END*********")
            log.info("*********TEST END*********\n\n")
            # fp.close()
        # 判断邮件发送的开关
        if on_off == 'on':
            mail = SendMail(
                username='zhouji@kedacom.com',
                passwd='7TmP9XC9',
                recv=[readConfig.ReadConfig().get_email('recv')],
                title=readConfig.ReadConfig().get_email('title'),
                content=readConfig.ReadConfig().get_email('content'),
                file=['C:/Users/admin/PycharmProjects/interfaceTest/result/logs',
                      'C:/Users/admin/PycharmProjects/interfaceTest/result/测试报告.html'],
                ssl=False,
            )
            mail.send_mail()
        elif on_off == 'off':
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")
            log.info("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告\n\n")
        else:
            print("邮件发送开关配置错误！！！")
            log.info("邮件发送开关配置错误！！！\n\n")

# pythoncom.CoInitialize()
# scheduler = BlockingScheduler()
# scheduler.add_job(AllTest().run, 'cron', day_of_week='1-5', hour=14, minute=59)
# scheduler.start()


if __name__ == '__main__':
    AllTest().run()


