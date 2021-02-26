class GlobalVar:

    def __init__(self):  # 初始化参数
        global _global_dict  # 定义全局变量
        _global_dict = {}  # 变量格式为字典

    def set_value(self, name, value):  # 定义存入value方法
        _global_dict[name] = value  # 存入对应key的value

    def get_value(self, name, defvalue=None):  # 定义获取value的方法
        try:
            return _global_dict[name]
        except KeyError:  # 异常处理机制
            return defvalue
