import selenium 
import os 
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def verifica_actualizaciones(url, path_driver):
    
    os.chdir(path_driver)

    driver = webdriver.Edge()

    driver.maximize_window()

    driver.get(url)

    try:
        el_encino_mazatlan = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div/a/h2[contains(text(), "El Encino")]')))

        #print(el_encino_mazatlan.text)
        
        el_encino_mazatlan.click()

        condiciones_operativas = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="menu-item"]/a[contains(text(), "Condiciones Operativas")]' ))).click()

        #print(condiciones_operativas.text)

        calidad_gas = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="menu-item"]/a[contains(text(), "Calidad de Gas")]' )))

        calidad_gas.click()

        fecha_ultimo_registro = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="loadedContent"]/div[@class="row"][3]/div[2]' )))

        print(fecha_ultimo_registro.text)

        #time.sleep(5)
        return fecha_ultimo_registro

    finally:
        driver.quit()

url = 'http://www.tcmas.mx/'
path_driver = r"C:\Users\Ernesto\Desktop\ServicioSocial\web_drivers"

fecha = verifica_actualizaciones(url, path_driver)

print(fecha)