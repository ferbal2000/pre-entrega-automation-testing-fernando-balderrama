import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture

# Configuración del driver (Chrome)
def driver():
    # Servicio de Chrome
    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless") #(descomentar para usar sin interfaz gráfica)

    # Inicializar driver
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    driver.quit()
