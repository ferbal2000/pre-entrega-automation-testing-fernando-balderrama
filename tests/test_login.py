import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.autenticacion import iniciar_sesion
from config import (
    TIEMPO_ESPERA,
    USUARIO_VALIDO,
    CONTRASENA_VALIDA
)

def test_login_exitoso(driver):
    # Iniciar sesión con credenciales válidas
    iniciar_sesion(driver, USUARIO_VALIDO, CONTRASENA_VALIDA)

    espera = WebDriverWait(driver, TIEMPO_ESPERA)

    # Esperar hasta llegar a la página de inventario
    espera.until(
        EC.url_contains("/inventory.html")
    )

    # Validar que se haya redirigido al inventario. Comentar si se ejecuta en modo headless
    assert "/inventory.html" in driver.current_url, (
        "El login falló: no se redirigió al inventario"
    )

    # Esperar y validar el título Products
    titulo = espera.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titulo.text == "Products", (
        "El título de la página no es Products"
    )

    # Esperar y validar el logo Swag Labs
    logo = espera.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))
    )
    assert logo.text == "Swag Labs", (
        "El texto del logo no es Swag Labs"
    )

    time.sleep(5) # Mantener el browser abierto. Comentar si se ejecuta en modo headless
