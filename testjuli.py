# Objectiu del test:
# Aquest test comprova que, en seleccionar l'opció "Beginner" a la pàgina web,
# es mostri correctament el valor "120€". Si el valor és correcte, el test passa;
# si no, el test falla i ens avisa que el valor esperat no coincideix.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Aquí fem la fixture pel driver de Selenium -- sino me petava el test.
# Bàsicament, aquest codi prepara el navegador per obrir-lo quan faci falta.
@pytest.fixture
def driver():
    # O sigui, aquí inicialitzem Chrome. Assegura't que el "ruta_al_driver" sigui correcte!!
    driver = webdriver.Chrome(executable_path="ruta_al_driver")
    # Obrim la pàgina local amb la ruta exacta
    driver.get("file:///home/programmer/Descargas/cybersecweb/cybersecweb/Home%20-%20CyberSec.html")
    # El "yield" manté el navegador obert mentre el test es fa, 
    # i quan acaba, el "quit()" el tanca -- perquè si no, se'ns omple el PC de finestres obertes.
    yield driver
    driver.quit()

# Aquí és on es fa el test real
@pytest.mark.usefixtures("driver")
def test_begginner_value(driver):
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
