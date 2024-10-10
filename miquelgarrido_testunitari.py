from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador (por ejemplo, Chrome)
driver = webdriver.Chrome()

# Abrir la página web
driver.get("http://www.cibergrup1.cecti.iesmontsia.cat")

try:
    # Esperar hasta que el meta tag esté presente (hasta 10 segundos)
    meta_description = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//meta[@name='description']"))
    )
    
    # Obtener el valor del atributo content
    description_content = meta_description.get_attribute("content")

    # Mostrar el valor obtenido
    print(f"Meta description content: {description_content}")
    
except Exception as e:
    print(f"Error: {e}")

# Cerrar el navegador
driver.quit()
