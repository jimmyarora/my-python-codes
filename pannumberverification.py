from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import xlwings as xw
import xlrd
import random
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import datetime
import ctypes  
import os
path= os.path.dirname(os.path.abspath(__file__))
print(path+"\PanNo.xlsm")







def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)













file_location = (path+"\PanNo.xlsm") 
workbook = xlrd.open_workbook(file_location) 
sheet = workbook.sheet_by_index(0)


username = (sheet.cell_value(4,6))
password= (sheet.cell_value(5,6))
tan = (sheet.cell_value(6,6))
name= (sheet.cell_value(7,6))
chrome_driver_exe= (sheet.cell_value(8,6))
print(username)
print(password)
print(tan)




chrome_options = Options()  
chrome_options.add_argument("--headless")  

products=[]   
url='https://jimmyarora.github.io/cv/'+name
driver2 = webdriver.Chrome((chrome_driver_exe),options=chrome_options)  
openWeb = driver2.get(url)
html = driver2.page_source

soup = BeautifulSoup(html,'html.parser')
tags = soup('li')

for tag in tags:
    papita =(tag.string)
    products.append(papita)

date_C = ((products[2]))
current_date1 =  datetime.datetime.strptime(date_C, '%Y-%m-%d')
date_E = ((products[1]))
expiry_date3 = datetime.datetime.strptime(date_E, '%Y-%m-%d')  
    

Agentid= (products[0])
print(Agentid)

if Agentid==(username) and (expiry_date3 > current_date1):
    print("crry on")
    driver2.close()
    url='https://www.tdscpc.gov.in/app/login.xhtml'
    driver = webdriver.Chrome(chrome_driver_exe)
    openWeb = driver.get(url)

    driver.find_element_by_id('userId').send_keys(username)
    driver.find_element_by_id('psw').send_keys(password)
    driver.find_element_by_id('tanpan').send_keys(tan) 
    time.sleep(15)
    driver.find_element_by_id('clickLogin').click()
    url2 ='https://www.tdscpc.gov.in/app/ded/panverify.xhtml'
    time.sleep(3)
    driver.get(url2)






    list_of_number= [] 
 
 


    for row in range(sheet.nrows):
        number= (sheet.cell_value(row , 2))
        list_of_number.append(number)
        
    
    
    
    
    
    i = 1
    while i<=3000:
        panNo = (list_of_number[i])
        driver.find_element_by_id('pannumber').click()
        n = int(random.randint(0,1))
        time.sleep(0 + n)
        driver.find_element_by_id('pannumber').clear()
        m = int(random.randint(0,1))
        time.sleep(0 + m)
     
        driver.find_element_by_id('pannumber').send_keys(panNo)
        o = int(random.randint(0,1))
        time.sleep(0.25 + o)
    
    
        driver.find_element_by_xpath("//*[@id='frmType1']/option[2]").click()
        p = int(random.randint(0,1))
        time.sleep(1 + p)
        driver.find_element_by_id('clickGo1').click()
        time.sleep(1 + n)
        name = driver.find_element_by_id('name').text
        status = driver.find_element_by_id('status').text
        add = i + 1
        intzrD= str(add)
        Dcolum = "D" + (intzrD)#D1 cell
        Ecolum = "E" + (intzrD)#E1 cell 
        wb = xw.Book(path+"\PanNo.xlsm")
        sht1 = wb.sheets['Sheet1']
        sht1.range(Dcolum).value = name
        sht1.range(Ecolum).value = status
     

    
        print(name)
        i += 1
        

    
else:
    print("ur software is expired")

    Mbox('Error', 'Your Software is Expired Plz Contact us at 7988994210', 1)
    
    
print("work complete")  




