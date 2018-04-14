import requests
import webbrowser
import ssl
from urllib.request import urlretrieve
import os

ssl._create_default_https_context = ssl._create_unverified_context

param = {'wd' : '海贼王'}
r = requests.get('http://www.baidu.com/s', params = param)
print(r.url)
webbrowser.open(r.url)

url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
# Method 1 简单就是下下来用urlretrieve
os.makedirs('./img/', exist_ok =True)

urlretrieve(url, './img/image1.png')

# Method 2 所有写好 放进内存 在一起存
r = requests.get(url)
with open('./img/image2.jpg','wb') as f:
	f.write(r.content)

# Method 3 下了多少 立马存多少 参数就是Stream
r = requests.get(url, stream = True)
with open('./img/image3.png', 'wb') as f:
	for chunk in r.iter_content(chunk_size=32): #chunk size 每次写入多少字节
		f.write(chunk)



