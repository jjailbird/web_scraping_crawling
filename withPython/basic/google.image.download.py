# -*- coding: utf-8 -*- 

from google_images_download import google_images_download
import os

WEBDRIVER_PATH_ABS = os.path.abspath(os.path.join(os.path.join(__file__, '..'),'../webdriver/chromedriver.exe')) 

def imageCrawling(keyword, directory):
  response = google_images_download.googleimagesdownload()
  arguments = {
    "keywords": keyword, 
    "limit": 200, 
    "print_urls": True, 
    "output_directory": directory,
    "chromedriver": WEBDRIVER_PATH_ABS
  }
  paths = response.download(arguments)

imageCrawling("고구마", "./download")