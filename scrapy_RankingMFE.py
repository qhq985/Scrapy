import importlib
from urllib.request import urlopen
import re
import sys
from bs4 import BeautifulSoup
import ssl

importlib.reload(sys)

ssl._create_default_https_context = ssl._create_unverified_context
# if has Chinese, apply decode()

url = "https://www.quantnet.com/mfe-programs-rankings/"
html = urlopen(url).read().decode('utf-8')
# print(html)

soup = BeautifulSoup(html, features = "lxml")
print('[Head]:\n',soup.h1)
# print('\n', soup.p)

# print('\n[The all URLs are]:\n')
# all_href = soup.find_all('a')
# for l in all_href:
# 	print(l.get('href','default'))
# Or we can do as follows:
# all_href = [l.get('href','default') for l in all_href]
# print('\n', all_href)

print('\n[The Ranking Universities are]:\n')
all_University = soup.find_all('b')
ui = 0
for u in all_University:
	ui += 1
	if 30 >= ui >= 3:
		print('Rank{} is {}'.format(ui-2, u.get_text()))

# print('\n[All Informations are]:\n')
# all_information = soup.find_all('tr')
# for p in all_information:
# 	print('\n', p.get_text())

print('\n[All jpg links are]:\n')
img_links = soup.find_all('img', {'src': re.compile('.*?\.jpg')})
for link in img_links:
	print('https://www.quantnet.com/'+link['src'])

