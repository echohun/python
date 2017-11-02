import smtplib  
import email.mime.multipart  
import email.mime.text  
 
#建立邮件对象  
msg = email.mime.multipart.MIMEMultipart()  
#添加数据，来自哪，去哪
msg['Subject'] = u'标题' 
#邮件显示的发送人 
msg['From'] = 'xxx@xx.com'  
#接受地
msg['To'] = 'xxx@xx.com' 
#发送的内容  
content = "内容" 
    
txt = email.mime.text.MIMEText(content,'text','utf-8')   
# 将多个子部分进行组合 
msg.attach(txt)    
 
#防出错  
try:  
        smtp = smtplib.SMTP()
        # 连接到服务器
        smtp.connect('smtp.163.com', '25')
        # 用户名密码登录，密码为163邮箱的授权码，自己设置的
        smtp.login('代理邮箱', '授权码')
        # 发送邮件（发送地，接受地，内容） 第二个参数必须为列表
        smtp.sendmail('代理邮箱', ['目的邮箱'], msg.as_string()) 
        #退出
        smtp.quit()  
        print('邮件发送成功email has send out !')  
except Exception as e:
    #打印出错原因，可以查看出错代码  
    print(e)
