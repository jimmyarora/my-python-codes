from selenium import webdriver
from bs4 import BeautifulSoup
#from urllib2 import urlopen
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time





username = 'DR1374'
password='Pcapex0114'
url='https://kite.zerodha.com/connect/login?api_key=08nglzb8r52530hw&sess_id=ku6vBtpZE3HdEOEDOT1rZeB3uKQzF4VT'
driver = webdriver.Chrome("E:\chromedriver.exe")
openWeb = driver.get(url)
time.sleep(5)
driver.find_element_by_xpath("//input[@type='text']").send_keys(username)
driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
'''driver.find_element_by_xpath("//button[@type='submit']").click()


#driver2.find_element_by_id('Password').send_keys(password)
#driver2.find_element_by_name('submit').click()'''
