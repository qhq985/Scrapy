from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')  # define headless
  

# driver = webdriver.Chrome(chrome_options=chrome_options)   # 参数，这样就可已在后台运行了
driver = webdriver.Chrome()



driver.get("https://www.google.com/")
driver.find_element_by_id("lst-ib").click()
driver.find_element_by_xpath("//div[@id='sbse0']/div").click()
driver.find_element_by_link_text("Welcome to Python.org").click()
driver.find_element_by_link_text("Applications").click()
driver.find_element_by_link_text("BeautifulSoup").click()
driver.find_element_by_xpath("//h1").click()
driver.find_element_by_link_text("4.6/").click()
driver.find_element_by_link_text("Documentation").click()

html = driver.page_source
driver.get_screenshot_as_file('./img/screenshot1.png')
driver.close()
print(html[:200])