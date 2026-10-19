
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import (
    TIEMPO_ESPERA,
    USUARIO_VALIDO,
    CONTRASENA_VALIDA,
    TIEMPO_PAUSA_FINAL
)
from utils.autenticacion import iniciar_sesion
from utils.navegacion import esperar_inventario
from utils.pausas import pausar


def test_agregar_producto_al_carrito(driver):

    # Iniciar sesión con credenciales válidas
    iniciar_sesion(driver, USUARIO_VALIDO, CONTRASENA_VALIDA)
    esperar_inventario(driver)

    # Configurar el tiempo máximo de espera explícita
    espera = WebDriverWait(driver, TIEMPO_ESPERA)

    # Verificar que el carrito esté vacío inicialmente
    contador_inicial = driver.find_elements(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert len(contador_inicial) == 0, (
        "El carrito debería estar vacío antes de agregar productos"
    )

    # Esperar a que aparezca el primer producto
    primer_producto = espera.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    # Guardar el nombre del producto
    nombre_producto = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    assert nombre_producto, "El producto no tiene nombre"

    # Agregar el primer producto al carrito
    boton_agregar = primer_producto.find_element(
        By.CSS_SELECTOR, "button.btn_inventory"
    )
    boton_agregar.click()

    # Esperar y validar el contador del carrito
    contador = espera.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    # Guardar y validar la cantidad de productos
    cantidad_carrito = int(contador.text)

    assert cantidad_carrito == len(contador_inicial) + 1, (
        f"Se esperaba 1 producto en el carrito, pero aparecen {cantidad_carrito}"
    )

    # Abrir el carrito de compras
    link_carrito = driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    )
    link_carrito.click()

    # Esperar y validar la navegación al carrito
    espera.until(EC.url_contains("/cart.html"))

    assert "/cart.html" in driver.current_url, (
        "No se pudo acceder al carrito"
    )

    # Esperar que aparezca el producto en el carrito
    producto_carrito = espera.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    #Nombre del producto en el carrito
    nombre_carrito = producto_carrito.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    # Comprobar que sea el mismo producto
    assert nombre_carrito == nombre_producto, (
        f"Se esperaba '{nombre_producto}', pero aparece '{nombre_carrito}'"
    )

    print(f"Cantidad inicial de productos en el carrito: {len(contador_inicial)}")
    print(f"Producto agregado correctamente: {nombre_carrito}")
    print(f"Cantidad de productos en el carrito: {cantidad_carrito}")

    # Para observar las acciones en el browser.
    # Si se ejecuta en modo headless, cambiar a False MODO_VISUAL en config.py
    pausar(TIEMPO_PAUSA_FINAL)
