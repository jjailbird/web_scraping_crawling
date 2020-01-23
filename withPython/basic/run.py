# -*- coding: utf-8 -*- 
from selenium import webdriver

# 01. set parameter, agent, proxy, limit options
target_url = 'http://www.interpark.com/'
search_txt = '로마'

# 02. load driver
driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')
driver.implicitly_wait(5)
# 03. get url
driver.get(target_url)
# 04. input search key
search_input = driver.find_element_by_id('input_autoKeyword')
search_input.clear()
search_input.send_keys(search_txt)
# 05. click serach button
search_button = driver.find_element_by_xpath("//button[text()='검색']")
search_button.click()

# 06. wating until site load completed
# 07. cleanup temp files


