import selenium 
import os 
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def verifica_actualizaciones(url):

    path_driver = os.path.join(os.path.dirname(__file__), ".." , "web_driver")
    
    os.chdir(path_driver)

    driver = webdriver.Edge()

    driver.maximize_window()

    driver.get(url)

    try:
        el_encino_mazatlan = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div/a/h2[contains(text(), "El Encino")]')))

        #print(el_encino_mazatlan.text)
        
        el_encino_mazatlan.click()

        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="menu-item"]/a[contains(text(), "Condiciones Operativas")]' ))).click()

        #print(condiciones_operativas.text)

        calidad_gas = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="menu-item"]/a[contains(text(), "Calidad de Gas")]' )))

        calidad_gas.click()

        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@class="container-fluid"]/div[@class="loadedContent"]/div[@class="row"]/div[@class="tableColShaded col-lg-8 col-md-7 col-sm-6"]' )))

        for i in [1, 2, 3]:

            titulo = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
                (By.XPATH, f'//div[@class="container-fluid"]/div[@class="loadedContent"]/div[@class="row"][{i}]/div/a' )))
            print('bandera')
            print(titulo.text)

            if "fuera de" in titulo.text:
                 fecha_ultimo_registro = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
                (By.XPATH, f'//div[@class="container-fluid"]/div[@class="loadedContent"]/div[@class="row"][{i}]/div[2]' )))
                 break
            else:
                print('No hay fecha')

        #time.sleep(5)
        # print(fecha_ultimo_registro.text)
        return fecha_ultimo_registro.text

    finally:
        #driver.quit()
        print("aqui deberia cerrarse")

#url = 'http://www.tcmas.mx/'
#path_driver = r"C:\Users\Ernesto\Desktop\ServicioSocial\web_drivers"

#fecha = verifica_actualizaciones(url)

#print(fecha)
# fecha = verifica_actualizaciones('http://www.tcmas.mx/')

