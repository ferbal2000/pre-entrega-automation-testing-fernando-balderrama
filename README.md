# Automatización QA – SauceDemo

Proyecto de automatización de pruebas funcionales sobre [SauceDemo](https://www.saucedemo.com/), desarrollado como trabajo práctico utilizando Python, Selenium y pytest.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Selenium WebDriver:** automatización de interacciones con el navegador.
- **pytest:** ejecución y validación de casos de prueba.
- **pytest-html:** generación de reportes HTML.
- **webdriver-manager:** administración de ChromeDriver.

## Estructura del proyecto

```text
pre-entrega-qa/
├── tests/
│   ├── test_login.py
│   ├── test_catalogo.py
│   └── test_carrito.py
├── utils/
│   ├── autenticacion.py
│   ├── navegacion.py
│   └── pausas.py
├── reports/
│   └── reporte.html
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

### Descripción de los componentes

- `tests/`: contiene los casos de prueba automatizados.
- `utils/`: contiene funciones auxiliares reutilizables.
- `reports/`: almacena los resultados de las ejecuciones en formato HTML.
- `config.py`: centraliza las credenciales de prueba, URL, tiempos de espera y pausas visuales.
- `conftest.py`: configura el navegador mediante una fixture de pytest.
- `pytest.ini`: define las opciones predeterminadas de ejecución.
- `requirements.txt`: registra las dependencias del proyecto.

## Casos de prueba

### 1. Automatización de Login

Archivo: `tests/test_login.py`

- Navegar a la página de login de saucedemo.com.
- Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
- Validar login exitoso verificando que se haya redirigido a la página de inventario.
- Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs”.

### 2. Navegación y verificación del catálogo

Archivo: `tests/test_catalogo.py`

- Verificar que el título de la página de inventario sea correcto.
- Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno).
- Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
- Valida título.
- Valida presencia de productos.
- Lista nombre/precio del primero.

### 3. Interacción con productos

Archivo: `tests/test_carrito.py`

- Añadir un producto al carrito haciendo clic en el botón correspondiente.
- Verificar que el contador del carrito se incremente correctamente.
- Navegar al carrito de compras.
- Comprobar que el producto añadido aparezca correctamente en el carrito.
- Agrega primer producto.
- Verifica ítem en carrito.

## Instalación

**Requisitos previos:** Python, Google Chrome y Git.

1. Clonar el repositorio:

```bash
git clone https://github.com/ferbal2000/pre-entrega-automation-testing-fernando-balderrama.git
```

2. Ingresar al directorio:

```bash
cd pre-entrega-automation-testing-fernando-balderrama
```

3. Crear y activar el entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución de pruebas

Ejecutar todos los tests:

```bash
pytest
```

Ejecutar un caso de prueba específico:

```bash
pytest tests/test_login.py
pytest tests/test_catalogo.py
pytest tests/test_carrito.py
```

## Reportes HTML

La ejecución genera automáticamente el archivo:

```text
reports/reporte.html
```

Para generarlo manualmente:

```bash
pytest tests/ -v --html=reports/reporte.html --self-contained-html
```

Cada nueva ejecución sobrescribe el reporte anterior.

## Configuración

En `config.py` se encuentran las principales opciones del proyecto.

- `TIEMPO_ESPERA`: tiempo máximo de las esperas explícitas.
- `MODO_VISUAL`: activa o desactiva las pausas para observar las interacciones.
- `TIEMPO_PAUSA_CAMPOS`: duración de las pausas durante el login.
- `TIEMPO_PAUSA_FINAL`: pausa al finalizar los tests.
- `URL_BASE`: dirección de SauceDemo.

Para ejecutar sin pausas artificiales:

```python
MODO_VISUAL = False
```

Las pruebas utilizan esperas explícitas de Selenium para sincronizar las acciones con la interfaz.
