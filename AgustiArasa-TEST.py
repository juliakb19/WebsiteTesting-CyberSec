import pytest
import unittest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

class TestCORREU(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    def test_cORREU(self):
        self.driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")
        self.driver.find_element(By.LINK_TEXT, "Contacto").click()
        
        # DADES DEL CAMPS
        self.driver.find_element(By.ID, "form-field-name").send_keys("PACO")
        self.driver.find_element(By.ID, "form-field-email").send_keys("pppppp")
        valor_enviat = self.driver.find_element(By.ID, "form-field-email").get_attribute("value") #COMPROVA EL VALOR ENVIAT AL FORMULARI AL CAMP EMAIL
    
        # PATRO DE FORMAT QUE HA DE CONTENIR EL CORREU
        patro_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        self.driver.find_element(By.ID, "form-field-field_082047e").send_keys("666666666") #DADES DEL CAMP DE TELEFON
        self.driver.find_element(By.ID, "form-field-field_bbf37c1").send_keys("ASDASD") #DADES DE EMPRESA
        self.driver.find_element(By.ID, "form-field-message").send_keys("hola") #DADES DEL CAMP MISSATGE
        
        is_valid_email = re.match(patro_email, valor_enviat) is not None # COMPROVA QUE EL VALOR ENVIAT COMPLEIX EL REQUISIT DEL PATRO 
        self.assertTrue(is_valid_email, "El format del email es incorrecte.") #SINO COMPLEIX EL REQUISIT ENS DIRA QUE EL FORMAT DEL CORREU ES INCORRECTE I NO ENVIA EL CORREU

        # CLICA EL BOTO DE ENVIAR
        self.driver.find_element(By.CSS_SELECTOR, ".elementor-button-content-wrapper").click()
        sleep(5)

if __name__ == "__main__":
    unittest.main()
