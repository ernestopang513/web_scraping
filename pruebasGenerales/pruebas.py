
import selenium 
import os 
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By


#iniciar con url
url = 'http://demo-store.seleniumacademy.com/'
path_dirver = os.chdir('C:\Users\Ernesto\Desktop\ServicioSocial\web_drivers')

driver = webdriver.Edge(executable_path='webdriver')

driver.maximize_window()

time.sleep(10)