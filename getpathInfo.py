import os


def get_path():
    path = os.path.split(os.path.abspath(__file__))[0]  # 获取当前文件绝对路径
    return path  # 返回路径


if __name__ == '__main__':  # 执行该文件，测试下是否OK
    '''print('测试路径是否OK,路径为：', get_path())'''
