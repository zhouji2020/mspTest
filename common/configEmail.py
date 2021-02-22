from readConfig import ReadConfig
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64


class SendMail(object):
    def __init__(self, username, passwd, recv, title, content, file=None, ssl=False,
                 email_host='smtp.kedacom.com', port=25, ssl_port=995):
        self.username = ReadConfig().get_email('username')  # 用户名
        self.passwd = ReadConfig().get_email('passwd')  # 密码
        self.recv = ReadConfig().get_email('recv')  # 收件人，多个要传list ['a@qq.com','b@qq.com]
        self.title = ReadConfig().get_email('title')  # 邮件标题
        self.content = content  # 邮件正文
        self.file = file  # 附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = email_host  # smtp服务器地址
        self.port = port  # 普通端口
        self.ssl = ssl  # 是否安全链接
        self.ssl_port = ssl_port  # 安全链接端口

    def send_mail(self):
        msg = MIMEMultipart()  # 发送内容的对象
        if self.file:  # 处理附件的
            file_name = os.path.split(self.file)[-1]  # 只取文件名，不取路径
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！！')
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'  # base64.b64encode(file_name.encode()).decode()
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                # 这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' % new_file_name
                msg.attach(att)
        msg.attach(MIMEText(self.content))  # 邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = ','.join(self.recv)  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)  # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            pass
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')
        self.smtp.quit()


if __name__ == '__main__':
    m = SendMail(
        username='zhouji@kedacom.com',
        passwd='7TmP9XC9',
        recv=['fengpeng@kedacom.com'],
        title='拼控服务自动化测试报告',
        content='各位好，测试已完成，请查阅测试报告内容',
        file=r'C:\Users\admin\PycharmProjects\interfaceTest\result\logs',
        ssl=False,
    )
    m.send_mail()
