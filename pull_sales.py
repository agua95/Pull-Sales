#import packages I'll need
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import os
import keyboard
import pandas as pd
import getpass
from bs4 import BeautifulSoup

#Get username and password
uname = input("Username:")
pword = getpass.getpass("Password:")

#Open Chrome
driver = webdriver.Chrome()

#Go to login page and log in
driver.get(r'https://www.yardiaspla2.com/04030calam/pages/LoginAdvanced.aspx')

elem = driver.find_element_by_id('Username')
elem.clear()
elem.send_keys(uname)

#need to click on the "Password Text" field first
elem = driver.find_element_by_id('Password_Text')
elem.click()
elem = driver.find_element_by_id('Password')
elem.clear()
elem.send_keys(pword)

elem = driver.find_element_by_id('cmdLogin1')
elem.click()

#Enter username/password and click login

#Navigate to sales page
driver.get(r'https://www.yardiaspla2.com/04030calam/pages/SysSqlScript.aspx?action=report&select=reports%2frs_CalAm_Inventory_SalesReport_New.txt&hprop=510&dtfrom=10/1/2019&dtto=10/31/2019')


#Use pd.read_html to read the table into a dataframe
df = pd.read_html(driver.find_element_by_id("TableWriter1").get_attribute('outerHTML'))[0]

#Use pd.to_csv to save it as a csv somewhere
export_csv = df.to_csv (r'exported_data.csv', index = None, header=True)

#Close Chrome
driver.quit()
