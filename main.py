import unittest
import pytest
import time
import re
from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService  # Si usas ambos navegadores
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    
    
    yield driver
    driver.quit()

def test_formulari_email(driver):
    try:
        driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")
        
        driver.find_element(By.ID, "form-field-name").send_keys("Jordi Navarro Gómez")
        driver.find_element(By.ID, "form-field-field_082047e").send_keys("658748211")
        driver.find_element(By.ID, "form-field-field_bbf37c1").send_keys("IESMontsia")
        driver.find_element(By.ID, "form-field-message").send_keys("Test python")

        email_field = driver.find_element(By.ID, "form-field-email")
        email_field.send_keys("alumne@gmail.com") 
        email_value = email_field.get_attribute("value")
        
        assert email_value != "", "El campo d'email no pot estar buit"  

    except Exception as e:
        print(f"S'ha produït un error: {e}")
        assert False, "Error inesperat."
        

def test_correu(driver):
    try:
        driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Contacto").click()
        
        # DADES DEL CAMPS
        driver.find_element(By.ID, "form-field-name").send_keys("PACO")
        driver.find_element(By.ID, "form-field-email").send_keys("pppppp@gmail.com")
        valor_enviat = driver.find_element(By.ID, "form-field-email").get_attribute("value") # COMPROVA EL VALOR ENVIAT AL FORMULARI AL CAMP EMAIL

        # PATRO DE FORMAT QUE HA DE CONTENIR EL CORREU
        patro_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        driver.find_element(By.ID, "form-field-field_082047e").send_keys("666666666") # DADES DEL CAMP DE TELEFON
        driver.find_element(By.ID, "form-field-field_bbf37c1").send_keys("ASDASD") # DADES DE EMPRESA
        driver.find_element(By.ID, "form-field-message").send_keys("hola") # DADES DEL CAMP MISSATGE
        
        is_valid_email = re.match(patro_email, valor_enviat) is not None # COMPROVA QUE EL VALOR ENVIAT COMPLEIX EL REQUISIT DEL PATRO
        assert is_valid_email, "El format del email es incorrecte."  # Si no compleix el requisit, mostrará el missatge d'error.
        
        # CLICA EL BOTO DE ENVIAR
        driver.find_element(By.CSS_SELECTOR, ".elementor-button-content-wrapper").click()
        
        sleep(2)
    except Exception as e:
        print(f"Error inesperat: {e}")
        assert False, "S'ha produït un error inesperat en el test del formulari de correu."



def test_meta_description(driver):
    
    driver.get("http://www.cibergrup1.cecti.iesmontsia.cat")

    try:
        # Esperar hasta que el meta tag estigui present (10 segons)
        meta_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//meta[@name='description']"))
        )
        
        # Obtenim el valor de la meta description
        description_content = meta_description.get_attribute("content")

        # Mostrar el valor obtingut de la meta description
        print(f"Meta description content: {description_content}")
        
        # Verificar que la meta description 
        assert description_content is not None and description_content.strip() != "", "La meta descripción no se ha encontrado o está vacía"
    # SI FALLA EN TRY IMPRIMEIX EL ERROR    
    except Exception as e:
        print(f"Error: {e}")
    
    # TANCA EL NAVEGADOR
    driver.quit()


def test_click_button(driver):
    driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")
    sleep(2)

    try:
        # buscar el botón por la clase
        button = driver.find_element(By.CLASS_NAME, 'cmplz-deny')
        
        # Verificar si el botón fue encontrado
        assert button is not None, "Botó 'cmplz-deny' no trobat."

    except NoSuchElementException as e:
        print(f"Error: {e}")
        assert False, "Botó 'cmplz-deny' no trobat."

   
def test_robots(driver):
    try:
        driver.get('http://www.cibergrup1.cecti.iesmontsia.cat/contacto-equipo-de-expertos-en-ciberseguridad-en-amposta/')
        time.sleep(3)

        meta_tag = driver.find_elements(By.XPATH, "//meta[@name='robots']")

        if meta_tag:
            content = meta_tag[0].get_attribute('content')
            print(f"La etiqueta <meta name='robots'> amb valor: {content}")
        else:
            print("No hi ha l'etiqueta <meta name='robots'>")

    except Exception as e:
        print(f"Error inesperat: {e}")


def test_testKEvin(driver):
    try:
        driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")
        driver.maximize_window()
        driver.find_element(By.ID, "form-field-name").send_keys("Kevin")
        driver.find_element(By.ID, "form-field-email").send_keys("kevintroncho@iesmontsia.org")
        driver.find_element(By.ID, "form-field-field_082047e").send_keys("612345678")
        driver.find_element(By.ID, "form-field-field_bbf37c1").send_keys("institut")
        driver.find_element(By.ID, "form-field-message").send_keys("hola bon dia")
        sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".elementor-field-group .elementor-button-content-wrapper").click()
        sleep(5)
        page_source = driver.page_source
        assert "Your submission was successful." in page_source, "El mensaje de confirmación no se encontró en la página."
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        assert False, "Se produjo un error durante la prueba."


def test_Evaristo(driver):

    # Navegar a la página web http://www.cibergrup1.cecti.iesmontsia.cat
     #driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")
     #Nota: Como no consigo tener acceso a la pagina web del colegio para
     #poder realizar las pruebas he configurado la web www.tallerscornet.com para los mismos fines
     #es una página creado tb con wordpress.
         
    driver.get("http://www.tallerscornet.com/")
    
    # Esperar un poco para asegurarse de que la página esté completamente cargada
    time.sleep(5)
    
    # Obtener el contenido de la página y lo guardamos en body_text
    body_text = driver.find_element(By.TAG_NAME, "body").text
    
    
    # Comprobar si el correo electrónico está en el contenido de la página
    #email = "Info@cybersec.com"
    #Aqui miramos si existe el correo info@tallerscornet.com en lugar de Info@cybersec.com
    email="info@tallerscornet.com"

    #Lo pasaremos todo a minisculas para evitar errores en la comparación
    if email.lower() in body_text.lower():
        print(f"El correo electrónico {email} está presente en la página.")
    else:
        print(f"El correo electrónico {email} NO está presente en la página.")

    # Cerrar el navegador
    driver.quit()
    
