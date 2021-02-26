import readConfig

readconfig = readConfig.ReadConfig()


class geturlParams():  # 定义一个方法，将从配置文件中读取的进行拼接
    def get_url(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':' + \
                  readconfig.get_http('port')  # 拼接url
        return new_url  # 返回url


if __name__ == '__main__':  # 验证拼接后的正确性
    print(geturlParams().get_url())

