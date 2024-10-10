import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def driver():
    geckodriver_path = '/usr/local/bin/geckodriver'
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service)
    
    yield driver
    driver.quit()

def test_formulari_email(driver):
    driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")
    
    driver.find_element(By.ID, "form-field-name").send_keys("Jordi Navarro Gómez")
    driver.find_element(By.ID, "form-field-field_082047e").send_keys("658748211")
    driver.find_element(By.ID, "form-field-field_bbf37c1").send_keys("IESMontsia")
    driver.find_element(By.ID, "form-field-message").send_keys("Test python")

    email_field = driver.find_element(By.ID, "form-field-email")
    email_field.send_keys("alumne@gmail.com") 
    email_value = email_field.get_attribute("value")
    
    assert email_value != "", "El campo d'email no pot estar buit"
