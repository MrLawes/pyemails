# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback

class Email(object):

    @classmethod
    def get_mail_host(cls, from_user):
        '''
        from_user: 发件人的用户名
        '''
        if from_user.endswith('@qq.com'):
            return 'smtp.qq.com'
        raise 'set mail_host please'

    @classmethod
    def sendmail(cls, from_user,from_password,to_list,subject=u'标题',content=u'邮件内容',format='',file_name='',mail_host=''):
        '''
        from_user, from_password: 发件人的用户名和密码
        subject 邮件标题
        content base64编码后邮件内容(base64是防止乱码)
        file_name 附件，可空
        to_list 发送列表，如 ['abc@qq.com','efg@qq.com']
        sender_name 发送者名称
        mail_host 发件人的邮件host, 如 smtp.qq.com
        '''
        me = from_user + '<' + from_user + '>'
        msg = MIMEMultipart('alternative')
        content = content.encode('utf-8')
        if format == 'html':
            send_content = MIMEText(content, 'html', 'utf-8')
        else:
            send_content = MIMEText(content)
        msg.attach(send_content)
        if file_name.strip():
            mail_attach = MIMEText(open(file_name, 'rb').read(), 'base64', 'unicode')
            mail_attach["Content-Type"] = 'application/octet-stream'
            mail_attach["Content-Disposition"] = 'attachment; filename="%s"' % (file_name.encode('utf-8'))
            msg.attach(mail_attach)

        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            server = smtplib.SMTP()
            if mail_host:
                server.connect(mail_host)
            else:
                server.connect(cls.get_mail_host(from_user))
            server.login(from_user,from_password)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
        except:
            print traceback.format_exc()

sendmail = Email.sendmail