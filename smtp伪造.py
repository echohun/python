import smtplib  
import email.mime.multipart  
import email.mime.text  
 
#�����ʼ�����  
msg = email.mime.multipart.MIMEMultipart()  
#������ݣ������ģ�ȥ��
msg['Subject'] = u'����' 
#�ʼ���ʾ�ķ����� 
msg['From'] = 'xxx@xx.com'  
#���ܵ�
msg['To'] = 'xxx@xx.com' 
#���͵�����  
content = "����" 
    
txt = email.mime.text.MIMEText(content,'text','utf-8')   
# ������Ӳ��ֽ������ 
msg.attach(txt)    
 
#������  
try:  
        smtp = smtplib.SMTP()
        # ���ӵ�������
        smtp.connect('smtp.163.com', '25')
        # �û��������¼������Ϊ163�������Ȩ�룬�Լ����õ�
        smtp.login('��������', '��Ȩ��')
        # �����ʼ������͵أ����ܵأ����ݣ� �ڶ�����������Ϊ�б�
        smtp.sendmail('��������', ['Ŀ������'], msg.as_string()) 
        #�˳�
        smtp.quit()  
        print('�ʼ����ͳɹ�email has send out !')  
except Exception as e:
    #��ӡ����ԭ�򣬿��Բ鿴�������  
    print(e)
