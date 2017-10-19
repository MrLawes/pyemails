快速预览
* from pyemails import Email
* \# 申明用户名和密码及host, 腾讯企业邮箱：smtp.exmail.qq.com；需要设置 host='smtp.exmail.qq.com'
* email_obj = Email(user='example@qq.com', password='example', host='xxx')
* print email_obj.user,email_obj.password,email_obj.host
* \>\>\> example@qq.com, example, xxx
* \# 修改 host 
* email_obj.set_host(host='smtp.exmail.qq.com')
* print email_obj.user,email_obj.password,email_obj.host
* \>\>\> example@qq.com, example, smtp.exmail.qq.com
