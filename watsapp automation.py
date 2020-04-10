from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import xlwings as xw
import xlrd 


list_of_number= [] 
# Give the location of the file 
file_location = ("E:\watsapp.xlsx") 
  
# To open Workbook 
workbook = xlrd.open_workbook(file_location) 
sheet = workbook.sheet_by_index(0) 
  
# For row 0 and column 0 
 

for row in range(sheet.nrows):
    number= (sheet.cell_value(row, 0))
    
    list_of_number.append(number)
    #print(number)
     


def hasxpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


url='https://web.whatsapp.com/'
driver = webdriver.Chrome("E:\chromedriver.exe")
openWeb = driver.get(url)
time.sleep(40)
i = 0
while i<=2:
    username = int(list_of_number[i])
    msg = 'https://youtu.be/5sjZ-8ZhQ3s'
    
    search = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(username)
    time.sleep(7)
    
    
       
    if hasxpath("//*[@id='pane-side']/div[1]/div/div/div[2]")== True:
        
        time.sleep(5)
        
        driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[2]").click()
        time.sleep(5)
       
    
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").click()
        time.sleep(0.25)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(msg)
        time.sleep(10)
       
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
        time.sleep(5)
        i += 1
       
        
    else:
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='side']/div[1]/div/span/button").click()
        i += 1

       
   
    
   
        

    
        
        
  
  
 
'''username = 'prince'
msg = 'hello prince this is a automatic test msg send by python'
url='https://web.whatsapp.com/'
driver = webdriver.Chrome("E:\chromedriver.exe")
openWeb = driver.get(url)
time.sleep(25)
search = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(username)
time.sleep(0.25)
driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[1]").click()
time.sleep(0.25)
driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").click()
driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(msg)
driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()'''
#search.submit()
#time.sleep(2)
#search.send_keys('papita')
