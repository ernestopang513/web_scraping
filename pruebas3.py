import selenium 
import os 
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#iniciar con url
url = 'http://www.tcmas.mx/'
path_dirver = os.chdir(r"C:\Users\Ernesto\Desktop\ServicioSocial\web_drivers")

driver = webdriver.Edge()

driver.maximize_window()

driver.get(url)

try:
    el_encino_mazatlan = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div/a/h2[contains(text(), "El Encino")]')))

   

    print(el_encino_mazatlan.text)
    
    el_encino_mazatlan.click()

finally:
    driver.quit()
