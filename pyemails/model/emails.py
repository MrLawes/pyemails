# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback
from email.mime.image import MIMEImage


class Email(object):
    HTML = '<!DOCTYPE html><html lang="en"><body>{msg}</body></html>'

    def __init__(self, user, password, host=None):
        """
        :param user:        用户名
        :param password:    密码
        :param host:        邮箱的 host
        """
        if host == None:
            host = self.get_mail_host(user)
        self.host = host
        self.user = user
        self.password = password
        self._msg = ''

    def set_host(self, host):
        """ 修改 host
        :param host:
        :return:
        """
        self.host = host

    def add_mime_text(self, text):
        """ 添加内容
        :param text:
        :return:
        """
        self._msg = '<div>%s</div>' % (text)

    @property
    def msg(self):
        return self.HTML.format(msg=self._msg)

    def send(self, to_addrs, cc):
        """ 发送邮件
        :param to_addrs:    目标地址
        :param cc:          抄送
        :return:
        """
        if isinstance(to_addrs, basestring):
            to_addrs = [to_addrs]
        if isinstance(cc, basestring):
            cc = [cc]

        me = self.user + '<' + self.user + '>'
        msg = MIMEMultipart('related')
        server.sendmail(me, to_addrs + cc, msg.as_string())

    @classmethod
    def get_mail_host(cls, from_user):
        '''
        from_user: 发件人的用户名
        '''
        if from_user.endswith('@qq.com'):
            return 'smtp.qq.com'
        elif from_user.endswith('@163.com'):
            return 'smtp.163.net'
        elif from_user.endswith('@126.com'):
            return 'smtp.126.com'
        elif from_user.endswith('@yeah.net'):
            return 'smtp.yeah.net'
        elif from_user.endswith('@sina.cn'):
            return 'smtp.sina.com'
        elif from_user.endswith('@sina.com'):
            return 'smtp.sina.com'
        elif from_user.endswith('@yahoo.com'):
            return 'smtp.mail.yahoo.cn'
        elif from_user.endswith('@sohu.com'):
            return 'smtp.sohu.com'

        raise 'set mail_host please'

    @classmethod
    def sendmail(cls, from_user, from_password, to_list, subject=u'标题', content=u'邮件内容', format='', file_name='',
                 mail_host='', cc=None, img_list=None):
        '''
        from_user, from_password: 发件人的用户名和密码
        subject 邮件标题
        content base64编码后邮件内容(base64是防止乱码)
        file_name 附件，可空
        to_list 发送列表，如 ['abc@qq.com','efg@qq.com']
        sender_name 发送者名称
        mail_host 发件人的邮件host, 如 smtp.qq.com
        cc 抄送给谁, 如 ['abc@qq.com','efg@qq.com']
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
        if isinstance(to_list, basestring):
            to_list = [to_list]
        msg['To'] = ", ".join(to_list)
        if cc:
            if isinstance(cc, basestring):
                cc = [cc]
            msg['Cc'] = ', '.join(cc)
        try:
            server = smtplib.SMTP()
            if mail_host:
                server.connect(mail_host)
            else:
                server.connect(cls.get_mail_host(from_user))
            server.login(from_user, from_password)
            server.sendmail(me, to_list + cc, msg.as_string())
            server.close()
        except:
            print traceback.format_exc()


sendmail = Email.sendmail
