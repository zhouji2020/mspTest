import json
import unittest
import time
import geturlParams
from common.configHttp import RunMain

url = geturlParams.geturlParams().get_url()  # 调用我们的geturlParams获取我们拼接的URL
new_url = url + '/msp/api/v1/manage/system/login'
body = json.dumps({"user_name": "admin", "password": "admin"})


class TestCase(unittest.TestCase):
    def testlogin(self):
        info = RunMain().run_main('post', new_url, body)
        time.sleep(3)
        self.assertTrue(info)


if __name__ == "__main__":
    unittest.main()
