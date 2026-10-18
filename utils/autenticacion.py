from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.pausas import pausar

from config import (
    URL_BASE,
    TIEMPO_ESPERA,
    TIEMPO_PAUSA_CAMPOS
)

def iniciar_sesion(driver, usuario, contrasena):
    # Abrir la página de login
    driver.get(URL_BASE)

    # Configurar el tiempo máximo de espera explícita
    espera = WebDriverWait(driver, TIEMPO_ESPERA)

    # Esperar el campo de usuario e ingresar el nombre
    campo_usuario = espera.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    campo_usuario.send_keys(usuario)

    # Para observar las acciones en el browser.
    # Si se ejecuta en modo headless, cambiar a False MODO_VISUAL en config.py
    pausar(TIEMPO_PAUSA_CAMPOS)

    # Ingresar la contraseña
    campo_contrasena = driver.find_element(By.ID, "password")
    campo_contrasena.send_keys(contrasena)

    # Para observar las acciones en el browser.
    # Si se ejecuta en modo headless, cambiar a False MODO_VISUAL en config.py
    pausar(TIEMPO_PAUSA_CAMPOS)

    # Hacer click en botón login
    boton_login = driver.find_element(By.ID, "login-button")
    boton_login.click()
