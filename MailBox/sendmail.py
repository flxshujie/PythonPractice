#! /usr/bin/env python`
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.multipart import MIMEBase, MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

# 格式化一个邮件地址
def _format_addr(s):
    # parseaddr：解析字符串中的email地址
    name, addr = parseaddr(s)
    # name中包含中文，需要通过Header对象进行编码
    # formataddr:parseaddr函数的逆函数
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 登录账户和口令
from_addr = input('From：')
password = input('Password：')
# 目标地址
to_addr = input('To：')
# 目标服务器
smtp_server = input('SMTP server：')

# 封装邮件
# 内容
msg = MIMEText('Hello,send by Python...', 'plain', 'utf-8')
# HTML邮件
msg = MIMEText('<html><body><h1>Hello</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>', 'html', 'utf-8')
# 发件人
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
# 收件人
msg['To'] = _format_addr('管理员<%s>' % to_addr)
# 主题
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

# 邮件对象
msg = MIMEMultipart()
msg = MIMEMultipart('alternative')
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候。。。', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                    '<p><img src="cid:0"></p>' +
                    '</body></html>', 'html', 'utf-8'))

with open('/Users/yuedan/PycharmProjects/POS列表.jpg', 'rb') as f:
    # 设置附件和MIME，从本地读取一个图片
    mime = MIMEBase('image', 'jpeg', filename='POS列表.jpg')
    # 加上必要的头信息：
    mime.add_header('Content-Disposition', 'attachment', filename='POS列表.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来：
    mime.set_payload(f.read())
    # 用Base64编码：
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
try:
    # 发送邮件
    # 创建服务器
    server = smtplib.SMTP_SSL(smtp_server, 465)
    # 打印出和SMTP服务器所有的交互信息
    server.set_debuglevel(1)
    # 登录服务器
    server.login(from_addr, password)
    # 发送邮件
    # 发件账户，收件账户，内容
    server.sendmail(from_addr, [to_addr], msg.as_string())
    # 退出服务器
    server.quit()
    print('Success!')
except smtplib.SMTPException as e:
    print('Fail,%s' % e)
