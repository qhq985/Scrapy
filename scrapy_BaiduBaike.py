import importlib
from urllib.request import urlopen
import re
import sys
from bs4 import BeautifulSoup
import ssl
import random	


ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://baike.baidu.com"
history = [base_url + '/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711']

for i in range(8):
	url = history[-1]
	html = urlopen(url).read().decode('utf-8')
	soup = BeautifulSoup(html, features = 'lxml')
	print('[{}]{}: {}'.format(i+1, soup.find('h1').get_text(),history[-1]))	

	# find valid urls
	sub_urls = soup.find_all('a', {'target':'_blank', 'href': re.compile('/item/(%.{2})+$')})
	if len(sub_urls)!= 0:
		history.append(base_url + random.sample(sub_urls, 1)[0]['href'])
	else:
		# No valid sub link found
		history.pop()

