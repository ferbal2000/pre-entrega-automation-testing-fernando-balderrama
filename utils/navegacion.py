from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import TIEMPO_ESPERA

def esperar_inventario(driver):
    # Esperar que se cargue el inventario
    espera = WebDriverWait(driver, TIEMPO_ESPERA)

    espera.until(
        EC.url_contains("/inventory.html")
    )

    # Esperar que se muestre el título del catálogo
    titulo = espera.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    return titulo
