from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from utils.pausas import pausar
from utils.navegacion import esperar_inventario
from utils.autenticacion import iniciar_sesion

from config import (
    TIEMPO_ESPERA,
    USUARIO_VALIDO,
    CONTRASENA_VALIDA,
    TIEMPO_PAUSA_FINAL
)

def test_verificar_catalogo(driver):
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

    # Obtener los productos visibles del catálogo
    productos = espera.until(
        EC.visibility_of_any_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    assert len(productos) > 0, (
        "No se encontraron productos visibles en el catálogo"
    )

    # Obtener el nombre y precio del primer producto
    primer_producto = productos[0]

    nombre = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    precio = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    # Validar que el nombre y precio tengan contenido
    assert nombre, "El primer producto no tiene nombre"
    assert precio, "El primer producto no tiene precio"

    # Mostrar información del primer producto
    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")

    # Validar que el menú esté visible
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed(), "El menú no está visible"

    # Validar que el filtro esté visible
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed(), "El filtro no está visible"

    # Para observar las acciones en el browser.
    # Si se ejecuta en modo headless, cambiar a False MODO_VISUAL en config.py
    pausar(TIEMPO_PAUSA_FINAL)
