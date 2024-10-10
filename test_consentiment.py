import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class testTancarCookies(unittest.TestCase):
    
    def setUp(self):

        # inicialitzar el driver del teu navegador
        self.driver = webdriver.Chrome()

        # url a comprovar
        self.url = "http://www.cibergrup1.cecti.iesmontsia.cat/"

    def test_click_button(self):
        driver = self.driver
        driver.get(self.url)
        sleep(2)

        # buscar el botó per la classe
        try:

            button = driver.find_element(By.CLASS_NAME, 'cmplz-deny')
            sleep(2)
            
            # clicar el botó
            button.click()
            sleep(2)
            
        # si no troba el botó, falla
        except NoSuchElementException:
            self.fail("Botó 'cmplz-deny' no trobat.")


if __name__ == "__main__":
    unittest.main()