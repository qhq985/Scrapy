import requests
import webbrowser
import ssl
from urllib.request import urlopen
import os
import sys
from bs4 import BeautifulSoup
import importlib
import time

importlib.reload(sys)
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://daily.zhihu.com/'

os.makedirs('./img/%s' % time.strftime('%d-%m-%Y'), exist_ok =True)

# html = requests.get(url).text
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, features = 'lxml')
img_ul = soup.find_all('div', {"class": "box"})
i = 0
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        i += 1
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s/%s'%(time.strftime('%d-%m-%Y'), image_name), 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved%d %s' %(i, image_name))