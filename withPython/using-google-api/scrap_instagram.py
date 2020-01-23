from seleniumrequestshtml import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import urllib.parse
import urllib.request
import time
import datetime
import csv

def scroll_down(webdriver):
    webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

def add_photo(webdriver) :
    temp_list = []
    one_photo = webdriver.find_elements_by_class_name("FFVAD")
    for n in one_photo:
        temp = {}
        temp['alt'] = n.get_attribute('alt')
        temp['src'] = n.get_attribute('src')
        temp_list.append(temp)
    return temp_list
#넘어오는 형식은 [{alt:내용, src:주소1},{alt:내용, src:주소}]

#검색을 원하는 insta ID
insta_id = input("Input Your Insta ID : ")
url = "https://www.instagram.com/" + insta_id

webdriver = Chrome('../chromedriver.exe')
webdriver.get(url)
session = webdriver.requests_session
response = session.get(url)

#포스트의 총 개수
len_post = webdriver.find_element_by_class_name('g47SY').text

photo_list = []
try:
    while True:
        for n in add_photo(webdriver):
            if n in photo_list:
                pass
            else:
                photo_list.append(n)

        scroll_down(webdriver)

        if(int(len_post) == len(photo_list)):
            break
except:
    pass
for i, n in enumerate(photo_list):
    urllib.request.urlretrieve(n['src'],str(i)+'.jpg')