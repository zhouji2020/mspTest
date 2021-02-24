import requests
import json
from common.Log import logger

logger = logger  # 新建logger方法的对象


class RunMain:

    def send_post(self, url, data):  # 定义post方法，传入需要的参数url和data
        result = requests.post(url=url, data=data)  # 得到原汁原味的接口返回
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result  # 返回接口返回的内容

    def send_get(self, url, data):  # 定义get方法，传入需要的参数url和data
        result = requests.get(url=url, data=data)  # 得到原汁原味的接口返回
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result  # 返回接口返回的内容

    def send_json_post(self, url, data):  # 定义json_post方法，传入需要的参数url和data
        result = requests.post(url=url, data=data).json()  # 得到json化的接口返回
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        # 将Python对象编码成JSON字符串，可以显示中文，按照首字母排序，首行缩进2位
        return res  # 返回JSON字符串

    def send_json_get(self, url, data):  # 定义json_get方法，传入需要的参数url和data
        result = requests.get(url=url, data=data).json()  # 得到json化的接口返回
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        # 将Python对象编码成JSON字符串，可以显示中文，按照首字母排序，首行缩进2位
        return res  # 返回JSON字符串

    def run_main(self, method, url=None, data=None, json=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None  # 初始化接口响应内容
        if method == 'post':  # 判断接口使用方法为post

            if json == 'no':  # 判断响应内容不为json格式
                result = self.send_post(url, data)  # 获取响应内容
                logger.info('响应状态码为：' + str(result.status_code))  # 将响应状态码打印至日志中
                logger.info('响应时间为：' + str(result.elapsed.total_seconds())+'s')  # 将响应时间打印至日志中

            elif json == 'yes':  # 判断响应内容为json格式
                result = self.send_json_post(url, data)  # 获取响应内容
                logger.info(str(result))  # 将响应内容打印至日志中

            else:
                print("json值错误！！！")
                logger.info("json值错误！！！")

        elif method == 'get':  # 判断接口使用方法为get

            if json == 'no':  # 判断响应内容不为json格式
                result = self.send_get(url, data)  # 获取响应内容
                logger.info('响应状态码为：' + str(result.status_code))  # 将响应状态码打印至日志中
                logger.info('响应时间为：' + str(result.elapsed.total_seconds()) + 's')  # 将响应时间打印至日志中

            elif json == 'yes':  # 判断响应内容为json格式
                result = self.send_json_post(url, data)  # 获取响应内容
                logger.info(str(result))  # 将响应内容打印至日志中

            else:
                print("json值错误！！！")
                logger.info("json值错误！！！")

        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")

        return result


if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确（需要先运行起test_api.py模块）
    result1 = RunMain().run_main('post', 'http://127.0.0.1:8888/login', {'name': 'xiaoming', 'pwd': '111'}, 'no')
    result2 = RunMain().run_main('get', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=111', 'yes')
    print(result1)
    print(type(result1))
    print(result1.status_code)
    print(str(result1.elapsed.total_seconds())+'s')
    print(result2)
    print(type(result2))
