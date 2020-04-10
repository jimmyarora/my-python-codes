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

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

username = 'jimmy.arora95@gmail.com'
password='iluvmusic'
url2='https://www.facebook.com/'
driver2 = webdriver.Chrome("E:\chromedriver.exe")
openWeb2 = driver2.get(url2)
driver2.find_element_by_id('email').send_keys(username)
driver2.find_element_by_id('pass').send_keys(password)    
driver2.find_element_by_id('loginbutton').click()
time.sleep(10)
driver2.execute_script("window.open('https://m.facebook.com/rohtaknewslive/photos/a.305047236309952/749115351903136/?type=3&source=48')")

driver2.switch_to.window(driver2.window_handles[1])





time.sleep(10)
html = driver2.page_source

i = 1
while i < 4:
  driver2.find_element_by_xpath("//*[@id='see_next_749115351903136']/a").click()
  time.sleep(5)

  i += 1
    
driver2.find_element_by_xpath("//*[@id='see_next_749115351903136']/a").click()   
time.sleep(5)

elements = driver2.find_elements_by_xpath("//div[@data-sigil='comment-body']")
for element in elements:
    papita= (element.text)
    print(papita.translate(non_bmp_map))



print("wrk is completed")




