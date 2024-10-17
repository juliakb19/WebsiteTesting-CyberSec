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
        #driver.find_element(By.ID, "form-field-email").send_keys("jordi@iesmontsia.org")

        driver.find_element(By.CSS_SELECTOR, ".elementor-field-group .elementor-button-content-wrapper").click()


        email_field = driver.find_element(By.ID, "form-field-email")
        validation_message = email_field.get_attribute("validationMessage")
        assert validation_message == "Please fill out this field.", \
                f"El mensaje de validación esperado no apareció. Se encontró: '{validation_message}'"

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

    # Buscar la pàgina web
    driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")

    # Sleep per a que carregui
    sleep(2)

    try:
        # buscar el botó per la clase
        button = driver.find_element(By.CLASS_NAME, 'cmplz-deny')
        
        # Verificar si el botó s'ha trobat
        assert button is not None, "Botó 'cmplz-deny' no trobat."

    except NoSuchElementException as e:

        # Mostrar error
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
        assert "Your submission was successful." in page_source, "El missatge de confirmació no s'ha trobat."
    
    except Exception as e:
        print(f"Ha sorgit un error {e}")
        assert False, "S'ha produit un error durant la prova."


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
    driver.quit() #ja no es fa falta
    # Comprobar si el correo electrónico está en el contenido de la página
    email = "Info@cybersec.com"
    #Aqui miramos si existe el correo info@tallerscornet.com en lugar de Info@cybersec.com
    #email="info@tallerscornet.com"

    #Lo pasaremos todo a minisculas para evitar errores en la comparación
    #assert: Si no contiene el correo dentro del body detendra la ejecucion de la funcion y mostrará el mensaje de error
    assert email.lower() in body_text.lower(), f"El correo electrónico {email} NO está presente en la página."

    # Si el correo está presente, el código sigue y muestra el mensaje
    print(f"El correo electrónico {email} está presente en la página.")
    
def test_preu_beginner(driver):
    driver.get("http://www.cibergrup1.cecti.iesmontsia.cat/")
    driver.execute_script("window.scrollBy(0, 2500);")

    sleep(2)
    # Fem clic al botó de "Beginner" -- com el trobem? Doncs amb l'XPATH que diu on està al codi HTML.
    begginner_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Beginner']/.."))
    )
    # Un cop trobat, el fem clic -- com si ho fessis tu amb el ratolí!
    begginner_button.click()

    # Ara busquem el text que ens ha de sortir quan seleccionem "Beginner".
    # Hauria de dir "120€", així que li diem al codi que trobi exactament això.
    result_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='120€']"))
    )
    # Agafem el text que ha trobat per comprovar si realment és "120€"
    result_text = result_element.text

    # El "assert" és com un exàmen. Aquí diu:
    # "Si el text NO és '120€', fes-me un error que diu 'Ei, el valor no és 120€ per beginner, és {result_text}'".
    # És com dir-li: "Si em falles, fes-ho amb estil".
    assert result_text == "120€", f"Ei, el valor no és 120€ per beginner, és {result_text}"
