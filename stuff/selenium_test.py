#!/usr/bin/env python3.6
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://{}'.format(os.environ.get('SQUASH_DOMAIN', '')))
try:
    driver.find_element_by_id("ID")
    driver.close()
    sys.exit(0)
except NoSuchElementException:
    sys.exit(1)
