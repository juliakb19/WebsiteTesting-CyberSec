import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Configuración del driver de Firefox sin opciones adicionales
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

def test_preu_beginner():
    # Carregar la pàgina
    driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")

    # Desplaçar-se cap avall en la pàgina
    driver.execute_script("window.scrollBy(0, 2500);")
    sleep(2)  # Pausa per assegurar que la pàgina ha carregat després del desplaçament

    # Trobar i fer clic en el botó "Beginner"
    begginner_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Beginner']/.."))
    )
    begginner_button.click()

    # Buscar el resultat que hauria de mostrar "120€"
    result_element = Web

def test_preu_beginner():
    # Carregar la pàgina
    driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")

    # Desplaçar-se cap avall en la pàgina
    driver.execute_script("window.scrollBy(0, 2500);")
    sleep(5)  # Pausa per assegurar que la pàgina ha carregat després del desplaçament

    # Trobar i fer clic en el botó "Beginner"
    begginner_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Beginner']/.."))
    )
    begginner_button.click()

    # Buscar el resultat que hauria de mostrar "120€"
    result_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='120€']"))
    )
    result_text = result_element.text

    # Comprovar que el valor mostrat sigui "120€"
    assert result_text == "120€", f"Ei, el valor no és 120€ per beginner, és {result_text}"

    # Tancar el navegador en finalitzar el test
    driver.quit()

# Crida a la funció per executar el test
test_preu_beginner()
