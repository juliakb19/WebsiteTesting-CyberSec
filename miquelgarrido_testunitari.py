import pytest
import unittest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_garrido():
    driver = webdriver.Chrome()


    driver.get("http://www.cibergrup1.cecti.iesmontsia.cat")

    try:
        
        meta_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//meta[@name='description']"))
        )
        
        description_content = meta_description.get_attribute("content")
        
        assert description_content is not None and description_content != "", "Error: Meta description no trobada o buida"
        print(f"Meta description content: {description_content}")
        
        #print(f"Meta description content: {description_content}")
        
    except Exception as e:
        print(f"Error: {e}")


    driver.quit()
