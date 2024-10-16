from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializar el controlador de Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navegar a la página web
     driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")
    
    
    
    # Esperar un poco para asegurarse de que la página esté completamente cargada
    time.sleep(5)

new_func()

    # Obtener el contenido de la página
    body_text = driver.find_element(By.TAG_NAME, "body").text

    # Comprobar si el correo electrónico está en el contenido de la página
    email = "info@celenium.com"
    
    if email in body_text:
        print(f"El correo electrónico {email} está presente en la página.")
    else:
        print(f"El correo electrónico {email} NO está presente en la página.")

finally:
    # Cerrar el navegador
    driver.quit()