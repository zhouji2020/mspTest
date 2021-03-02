import os

import frozen_dir
import getpathInfo  # 自己定义的内部类，该类返回项目的绝对路径
from xlrd import open_workbook  # 调用读Excel的第三方库xlrd

path = frozen_dir.app_path()  # 拿到该项目所在的绝对路径


class readExcel():
    def get_xls(self, xls_name, sheet_name):  # xls_name填写用例的Excel文件名称 sheet_name该Excel的sheet名称
        cls = []
        xls_path = os.path.join(path, "testFile", 'case', xls_name)  # 获取用例文件路径
        file = open_workbook(xls_path)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        nrows = sheet.nrows  # 获取这个sheet内容行数
        for i in range(nrows):  # 根据行数做循环
            if sheet.row_values(i)[0] != 'case_name':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':  # 我们执行该文件测试一下是否可以正确获取Excel中的值
    '''print(readExcel().get_xls('userCase.xlsx', 'Authentication'))
    print(readExcel().get_xls('userCase.xlsx', 'Authentication')[0])
    print(readExcel().get_xls('userCase.xlsx', 'Authentication')[1])'''
