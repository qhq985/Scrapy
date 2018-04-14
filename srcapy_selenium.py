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


driver.implicitly_wait(10)


driver.get("http://www.baidu.com/")
driver.find_element_by_id("kw").click()

driver.find_element_by_id("kw").clear()

driver.find_element_by_id("kw").send_keys(u"海贼王")
time.sleep(1) #这个必须加
driver.find_element_by_id("kw").send_keys(Keys.ENTER)

driver.find_element_by_link_text(u"海贼王_百度百科").click()

html = driver.page_source
driver.get_screenshot_as_file('./img/screenshot1.png')
driver.close()
print(html[:200])
