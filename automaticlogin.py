from selenium import webdriver
from bs4 import BeautifulSoup
#from urllib2 import urlopen
import pandas as pd
from selenium.webdriver.common.keys import Keys


#import requests
#import urllib.request
#import time
#from bs4 import BeautifulSoup

#username='jimmy@dopagent.com'
#password='@@yushi'

'''products=[]   
url='https://jimmyarora.github.io/cv/'
driver = webdriver.Chrome("E:\chromedriver.exe")
openWeb = driver.get(url)
html = driver.page_source
#soup = BeautifulSoup(html)
soup = BeautifulSoup(html,'html.parser')
tags = soup('li')

for tag in tags:
    papita =(tag.string)
    products.append(papita)
    
    
print(products)    
jai = (products[6])'''
products=[] 
username = 'surajeng25@gmail.com'
password='Tm123456'
url2='https://www.apnapanindia.co.in/soft/Admin/index.php'
driver2 = webdriver.Chrome("E:\chromedriver.exe")
openWeb2 = driver2.get(url2)
driver2.find_element_by_id('email').send_keys(username)
driver2.find_element_by_id('Password').send_keys(password)    
driver2.find_element_by_name('submit').click()
#driver2.find_all('box_icon icon1').click()
#driver2.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
driver2.execute_script("window.open('https://www.apnapanindia.co.in/soft/Admin/user-power/profile.php', 'newwindow')")
driver2.switch_to.window(driver2.window_handles[1])
# element = driver2.find_element_by_name('OwnerName')
# papita= element.get_attribute('value')
# print(papita)
elements = driver2.find_elements_by_class_name('form-control')

for element in elements:
    papita= element.get_attribute('value')
    print(papita)
    products.append(papita)
    
    

print(products[4])


'''html = driver2.page_source
soup = BeautifulSoup(html,'html.parser')
for child in soup
print(soup.head.contents)'''


#tags = soup('value')
#print(tags)
'''for tag in tags:
    papita =(tag)
    print(papita)'''
     
    #products.append(papita)
    
    
#print(products)''' 


'''products.append(element)
print(products)
print("baabu baavdi hai")'''

'''url='http://34.209.100.24/admin'
driver = webdriver.Chrome("E:\chromedriver.exe")
openWeb = driver.get(url)
driver.find_element_by_name('email').send_keys(element)'''






    #print(tag.string)

#papita =(tag.string)
    
#print(papita)
#list(papita)
#print(papita[1])






#print (tag.get('li', None))

'''print(soup.li.string)'''





#driver.find_elementById("myLi");

#driver.find_element_by_name('email').send_keys(username)
#driver.find_element_by_id('STU_VALIDATE_WITHOUT_CAPTCHA').click()
#driver.find_element_by_id('AuthenticationFG.TARGET_CHECKBOX').click()
#driver.find_element_by_name('password').send_keys(password)
#driver.find_element_by_name('submit').click()
#x = driver.find_element_by_class('count').copy
#print(x)
