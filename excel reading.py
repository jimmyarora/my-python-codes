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
import pandas as pd
import xlrd 

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
     
     
print(list_of_number[3])    
    

