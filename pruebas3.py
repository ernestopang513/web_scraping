import selenium 
import os 
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By


#iniciar con url
url = 'http://www.tcmas.mx/'
path_dirver = os.chdir(r"C:\Users\Ernesto\Desktop\ServicioSocial\web_drivers")

driver = webdriver.Edge()

driver.maximize_window()

driver.get(url)
#time.sleep(2)
el_encino_mazatlan = driver.find_element(By.XPATH, '//div/a/h2[contains(text(), "El Encino")]')

#for i in el_encino_mazatlan:
#   print(i.text)

print(el_encino_mazatlan.text)
time.sleep(1)
el_encino_mazatlan.click()

#texto_1 = driver.find_element(By.XPATH, '//nav/ol/li/a[contains(text(), "Wo")]')

#print(texto_1.text)
time.sleep(10)