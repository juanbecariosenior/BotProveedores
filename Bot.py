from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración de Chrome para abrir en modo incógnito
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Habilita el modo incógnito

# Usar webdriver_manager para obtener y manejar automáticamente el ChromeDriver
service = Service(ChromeDriverManager().install())  # Este paso maneja la instalación y configuración del driver

def open_and_login(driver_number):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("")

    username_field = WebDriverWait(driver,5).until(
        EC.visibility_of_element_located((By.ID, "txtUsuario")) 
     )
    password_field = WebDriverWait(driver,5).until(
        EC.visibility_of_element_located((By.ID, "txtContrasena"))
    )  # Cambia el ID según sea necesario

    username_field.send_keys("")
    password_field.send_keys("")

    password_field.send_keys(Keys.RETURN)

    time.sleep(5)

    # Encuentra el elemento <a> que contiene el evento onmouseover
    hover_element = driver.find_element(By.XPATH, "//a[@onmouseover='popup(\"mainmenu\")']")

    # Crea una instancia de ActionChains
    actions = ActionChains(driver)

    # Realiza el hover sobre el elemento <a>
    actions.move_to_element(hover_element).perform()

    # Espera unos segundos para asegurarte de que el menú se despliegue
    time.sleep(3)

    menu_opcion = driver.find_element(By.ID, "el5")  # Cambia según tu menú
    menu_opcion.click()

    time.sleep(4)

    print(f"Login completado en ventana {driver_number}")

    return driver

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(open_and_login,i) for i in range(1,6)]

    for future in futures:
        future.result()
"""
# Abrir 20 ventanas en modo incógnito
windows = []
for _ in range(5):
    # Iniciar el navegador con el driver en modo incógnito
    driver = webdriver.Chrome(service=service, options=chrome_options)
    windows.append(driver)  # Guardar la referencia del driver de cada ventana

    # Abrir la página de login
    driver.get("https://proxyproveedoressears-gruposanborns.msappproxy.net/lib/login.asp")

for driver in windows:
    username_field = driver.find_element(By.ID, "IdUser")  # Cambia el ID según sea necesario
    password_field = driver.find_element(By.ID, "pas_Usuario")  # Cambia el ID según sea necesario

    username_field.send_keys("5592")
    password_field.send_keys("LIZ5595")

    password_field.send_keys(Keys.RETURN)














    # Esperar para que la página cargue
    #time.sleep(3)

    # Localiza los campos de usuario y contraseña por su nombre, id o algún otro selector
    username_field = driver.find_element(By.ID, "IdUser")  # Cambia el ID según sea necesario
    password_field = driver.find_element(By.ID, "pas_Usuario")  # Cambia el ID según sea necesario

    time.sleep(1)

    # Ingresa el usuario y la contraseña
    username_field.send_keys("5592")
    password_field.send_keys("LIZ5595")

    # Enviar el formulario (simular presionar Enter)
    password_field.send_keys(Keys.RETURN)

    dropdown_button = driver.find_element(By.CLASS_NAME,"dropdown-toggle")

    dropdown_button.click()

    time.sleep(2)

    dropdown_option = driver.find_element(By.LINK_TEXT, "Notas de Cargo")

    dropdown_option.click()

    # Esperar para ver la siguiente página
    time.sleep(5)

# Al final del script, no cerramos las ventanas, solo dejamos que queden abiertas.
# No se llama a driver.quit() o driver.close() para mantener las ventanas abiertas.
"""
