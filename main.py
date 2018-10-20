import urllib, urllib.request, sys
import ssl


host = 'https://api01.aliyun.venuscn.com'
path = '/ip'
method = 'GET'
appcode = '8528aa29626e4069b79690957937bffb'
querys = 'ip=113.87.18.88'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read().decode()
if (content):
    print(content)