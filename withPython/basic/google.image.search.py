# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support import expected_conditions as EC
import os
import base64

# 01. set parameter, agent, proxy, limit options >>>>>>>>>>>>>>>>>>>>>>>>>>>>
TARGET_URL = 'https://www.google.co.kr/imghp?hl=ko'
SEARCH_TXT = '고구마'
SEARCH_IPT_XPATH = '//*[@id="sbtc"]/div/div[2]/input'
SEARCH_BTN_XPATH = '//*[@id="sbtc"]/button'
SEARCH_RLT_ITEM_XPATH = '//a[@class="rg_l"]'
SEARCH_RLT_IMG_XPATH = '//img[@class="rg_ic rg_i"]'
#WEBDRIVER_PATH_ABS = Path(Path(__file__).parent).parent
WEBDRIVER_PATH_ABS = os.path.abspath(os.path.join(os.path.join(__file__, '..'),'../webdriver/chromedriver.exe')) 

print(WEBDRIVER_PATH_ABS)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 02. load driver >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH_ABS)
# driver.implicitly_wait(5)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 03. get url >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
driver.get(TARGET_URL)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 04. input search key >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
search_input = driver.find_element_by_xpath(SEARCH_IPT_XPATH)
search_input.clear()
search_input.send_keys(SEARCH_TXT)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 05. click serach button >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
search_button = driver.find_element_by_xpath(SEARCH_BTN_XPATH)
search_button.click()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 06. wating until site load completed
WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

search_result_items = driver.find_elements_by_xpath(SEARCH_RLT_ITEM_XPATH)
item_count = len(search_result_items)
print(str(item_count) + " items founded!")

num = 0
for item in search_result_items:
  num += 1
  file_name = SEARCH_TXT + format(num, '03') 
  img = item.find_element_by_xpath(SEARCH_RLT_IMG_XPATH)
    
  id = img.get_attribute('id')
  print(id)
  src_data = img.get_attribute('src')
  
  #print(str(num) + ":" + img)
  if src_data:
    img_data = base64.b64decode(src_data)
    
  # with open()
  else:
    print("no src")
  


# 07. cleanup temp files


