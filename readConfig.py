import os
import configparser
import getpathInfo  # 引入我们自己的写的获取路径的类

path = getpathInfo.get_path()  # 获取当前文件绝对路径
config_path = os.path.join(path, 'config.ini')  # 获取配置文件的绝对路径
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')  # 以utf-8编码读取配置文件


class ReadConfig:

    def get_http(self, name):  # 定义获取配置文件中session为http的配置内容
        value = config.get('HTTP', name)  # 获取session为HTTP，key为‘name’的配置内容
        return value  # 返回获取到的配置内容

    def get_email(self, name):
        value = config.get('EMAIL', name)  # 获取session为EMAIL，key为‘name’的配置内容
        return value

    def get_mysql(self, name):  # 写好，留以后备用。因为我们没有对数据库的操作，所以这个可以屏蔽掉
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
    '''print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('recv'))
    print(type(ReadConfig().get_email('recv')))'''
