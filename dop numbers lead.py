from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import xlwings as xw
import sys
import unicodedata

username = 'jimmy@dopagent.com'
password='@@yushi'
url2='https://www.dopagentsoftware.com/admin'
driver2 = webdriver.Chrome("E:\chromedriver.exe")
openWeb2 = driver2.get(url2)
driver2.find_element_by_xpath('//*[@id="loginForm"]/div[1]/input').send_keys(username)
driver2.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input').send_keys(password)    
driver2.find_element_by_xpath('//*[@id="loginForm"]/div[3]/input').click()
time.sleep(5)
driver2.execute_script("window.open('https://www.dopagentsoftware.com/admin/leads/index/0/?limit=100&search=&status=I&state=ALL&schedule_from=&schedule_to=&delivery_status=ALL&submit=Filter')")

driver2.switch_to.window(driver2.window_handles[1])







elements = driver2.find_elements_by_class_name("even pointer")
for element in elements:
    papita= (element.text)
    print(papita)


















