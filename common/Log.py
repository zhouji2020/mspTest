import datetime
import os
import logging
from logging.handlers import TimedRotatingFileHandler
import frozen_dir
import getpathInfo

path = getpathInfo.get_path()  # 根目录绝对路径
log_path = os.path.join(path, 'result')  # 存放log文件的路径
# now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')


class Logger(object):
    def __init__(self, logger_name='logs…'):  # 初始化参数
        self.logger = logging.getLogger(logger_name)  # 将名称为logger_name的Logger实例定义为一个对象
        logging.root.setLevel(logging.NOTSET)  # 不设置默认logging级别
        self.log_file_name = 'logs'  # 日志文件的名称
        self.backup_count = 5  # 最多存放日志的数量
        self.console_output_level = 'WARNING'  # 控制台输出级别
        self.file_output_level = 'DEBUG'  # 日志文件输出级别
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 日志输出格式

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()  # 将日志流输出到console_handler对象
            console_handler.setFormatter(self.formatter)  # 设置console_handler对象格式
            console_handler.setLevel(self.console_output_level)  # 设置console_handler对象日志等级
            self.logger.addHandler(console_handler)  # 将console_handler对象添加到日志处理中

            file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, self.log_file_name), when='D',
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            # 日志文件处理方式：每天重新创建一个日志文件，最多保留backup_count份
            file_handler.setFormatter(self.formatter)  # 日志文件格式
            file_handler.setLevel(self.file_output_level)  # 日志文件输出日志等级
            self.logger.addHandler(file_handler)  # 日志文件添加到日志处理中
        return self.logger  # 返回获取到的日志


logger = Logger().get_logger()  # 定义一个日志输出对象


# import os
# import logging
# from datetime import datetime
# import threading
#
# localReadConfig = readConfig.ReadConfig()
#
#
# class Log:
#     def __init__(self):
#         global logPath, resultPath, proDir
#         proDir = readConfig.proDir
#         resultPath = os.path.join(proDir, "result")
#         if not os.path.exists(resultPath):
#             os.mkdir(resultPath)
#         logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
#         if not os.path.exists(logPath):
#             os.mkdir(logPath)
#         self.logger = logging.getLogger()
#         self.logger.setLevel(logging.INFO)
#
#         # defined handler
#         handler = logging.FileHandler(os.path.join(logPath, "output.log"))
#         # defined formatter
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         handler.setFormatter(formatter)
#         self.logger.addHandler(handler)
#
#     def get_logger(self):
#         """
#         get logger
#         :return:
#         """
#         return self.logger
#
#     def build_start_line(self, case_no):
#         """
#         write start line
#         :return:
#         """
#         self.logger.info("--------" + case_no + " START--------")
#
#     def build_end_line(self, case_no):
#         """
#         write end line
#         :return:
#         """
#         self.logger.info("--------" + case_no + " END--------")
#
#     def build_case_line(self, case_name, code, msg):
#         """
#         write test case line
#         :param case_name:
#         :param code:
#         :param msg:
#         :return:
#         """
#         self.logger.info(case_name+" - Code:"+code+" - msg:"+msg)
#
#     def get_report_path(self):
#         """
#         get report file path
#         :return:
#         """
#         report_path = os.path.join(logPath, "report.html")
#         return report_path
#
#     def get_result_path(self):
#         """
#         get test result path
#         :return:
#         """
#         return logPath
#
#     def write_result(self, result):
#         """
#
#         :param result:
#         :return:
#         """
#         result_path = os.path.join(logPath, "report.txt")
#         fb = open(result_path, "wb")
#         try:
#             fb.write(result)
#         except FileNotFoundError as ex:
#             logger.error(str(ex))
#
#
# class MyLog:
#     log = None
#     mutex = threading.Lock()
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get_log():
#
#         if MyLog.log is None:
#             MyLog.mutex.acquire()
#             MyLog.log = Log()
#             MyLog.mutex.release()
#
#         return MyLog.log
#
# if __name__ == "__main__":
#     log = MyLog.get_log()
#     logger = log.get_logger()
#     logger.debug("test debug")
#     logger.info("test info")
