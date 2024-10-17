from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def test_Evaristo(driver):
    # Navegar a la página web http://www.cibergrup1.cecti.iesmontsia.cat
    driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")
    
     
     
     # Esperar explícitamente hasta que un elemento específico esté presente (ejemplo con el título de la página)
    try:
        # Espera hasta que el título de la página sea visible o hasta 10 segundos
        #Esta línea de código en Python, que utiliza Selenium, 
        # espera un máximo de 10 segundos O a que la página web haya terminado de cargarse por completo antes de proceder con el resto del script.
        #lo que antes ocurra.
        #https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.ui.html
        
        
        
        
        WebDriverWait(driver, 10).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        print("Página cargada completamente.")
        
    except Exception as e:
        assert false, (f"Ocurrió un error en la carga de la página: {e}")
    
    # Obtener el contenido de la página y lo guardamos en body_text
    body_text = driver.find_element(By.TAG_NAME, "body").text
    #print ({body_text})
     # Cerrar el navegador
    driver.quit()
    
    
    
    # Comprobar si el correo electrónico está en el contenido de la página
    email = "Info@cybersec.com"
    #Aqui miramos si existe el correo info@tallerscornet.com en lugar de Info@cybersec.com
    #email="info@tallerscornet.com"

    #Lo pasaremos todo a minisculas para evitar errores en la comparación
    #assert: Si no contiene el correo dentro del body detendra la ejecucion de la funcion
    assert email.lower() in body_text.lower(), f"El correo electrónico {email} NO está presente en la página."

# Si el correo está presente, el código sigue y muestra el mensaje
    print(f"El correo electrónico {email} está presente en la página.")
   



test_Evaristo(driver)   