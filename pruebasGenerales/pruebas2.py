import selenium 
import os 
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By


#iniciar con url
url = 'http://demo-store.seleniumacademy.com/'
path_dirver = os.chdir(r"C:\Users\Ernesto\Desktop\ServicioSocial\web_drivers")

driver = webdriver.Edge()

driver.maximize_window()

driver.get(url)

texto_1 = driver.find_element(By.XPATH, '//nav/ol/li/a[contains(text(), "Wo")]')

print(texto_1.text)
time.sleep(5)