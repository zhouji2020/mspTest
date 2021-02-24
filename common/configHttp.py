import requests
import json
from common.Log import logger

logger = logger


class RunMain:

    def send_post(self, url, data):  # 定义一个方法，传入需要的参数url和data，参数必须按照url、data顺序传入
        result = requests.post(url=url, data=data)  # .json()  # 因为这里要封装post方法，所以这里的url和data值不能写死
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def send_get(self, url, data):
        result = requests.get(url=url, data=data)  # .json()
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def send_json_post(self, url, data):
        result = requests.post(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_json_get(self, url, data):
        result = requests.get(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None, json=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            if json == 'no':
                result = self.send_post(url, data)
                logger.info('响应状态码为：' + str(result.status_code))
                logger.info('响应时间为：' + str(result.elapsed.total_seconds())+'s')
            elif json == 'yes':
                result = self.send_json_post(url, data)
                logger.info(str(result))

        elif method == 'get':
            if json == 'no':
                result = self.send_get(url, data)
                logger.info('响应状态码为：' + str(result.status_code))
                logger.info('响应时间为：' + str(result.elapsed.total_seconds()) + 's')
            elif json == 'yes':
                result = self.send_json_post(url, data)
                logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result


if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    result1 = RunMain().run_main('post', 'http://127.0.0.1:8888/login', {'name': 'xiaoming', 'pwd': '111'}, 'no')
    result2 = RunMain().run_main('get', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=111', 'yes')
    print(result1)
    print(type(result1))
    print(result1.status_code)
    print(str(result1.elapsed.total_seconds())+'s')
    print(result2)
    print(type(result2))
