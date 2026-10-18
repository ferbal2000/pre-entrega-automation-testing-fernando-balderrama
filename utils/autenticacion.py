from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URL_BASE, TIEMPO_ESPERA
import time

def iniciar_sesion(driver, usuario, contrasena):
    # Abrir la página de login
    driver.get(URL_BASE)

    # Configurar una espera explícita de 5 segundos
    espera = WebDriverWait(driver, TIEMPO_ESPERA)

    # Esperar el campo de usuario e ingresar el nombre
    campo_usuario = espera.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    campo_usuario.send_keys(usuario)
    time.sleep(2) # Para observar las acciones en el browser. Comentar si se ejecuta en modo headless

    # Ingresar la contraseña
    campo_contrasena = driver.find_element(By.ID, "password")
    campo_contrasena.send_keys(contrasena)
    time.sleep(2) # Para observar las acciones en el browser. Comentar si se ejecuta en modo headless

    # Hacer click en botón login
    boton_login = driver.find_element(By.ID, "login-button")
    boton_login.click()
