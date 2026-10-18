from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.pausas import pausar
from utils.autenticacion import iniciar_sesion
from utils.navegacion import esperar_inventario

from config import (
    TIEMPO_ESPERA,
    USUARIO_VALIDO,
    CONTRASENA_VALIDA,
    TIEMPO_PAUSA_FINAL
)

def test_login_exitoso(driver):
    # Iniciar sesión con credenciales válidas
    iniciar_sesion(driver, USUARIO_VALIDO, CONTRASENA_VALIDA)

    # Configurar el tiempo máximo de espera explícita
    espera = WebDriverWait(driver, TIEMPO_ESPERA)

    titulo = esperar_inventario(driver)

    # Validar que se haya redirigido al inventario.
    assert "/inventory.html" in driver.current_url, (
        "El login falló: no se redirigió al inventario"
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

    # Para observar las acciones en el browser.
    # Si se ejecuta en modo headless, cambiar a False MODO_VISUAL en config.py
    pausar(TIEMPO_PAUSA_FINAL)
