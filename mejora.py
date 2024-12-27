from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import logging
import time
import random

# Configuración del logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Configuración de Chrome para abrir en modo incógnito
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Habilita el modo incógnito

# Configuración del servicio del WebDriver
service = Service(ChromeDriverManager().install())

def open_and_login(driver_number):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    logging.info(f"Ventana {driver_number}: Navegador iniciado.")

    try:
        driver.get("")
        logging.info(f"Ventana {driver_number}: Página cargada.")

        time.sleep(2)

        if driver_number in [1,2,3]:

            # Esperar a los campos de usuario y contraseña
            username_field = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "txtUsuario"))
            )
            password_field = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "txtContrasena"))
            )
            logging.info(f"Ventana {driver_number}: Campos de login localizados.")

            time.sleep(2)

            username_field.send_keys("")
            password_field.send_keys("")
            password_field.send_keys(Keys.RETURN)
            logging.info(f"Ventana {driver_number}: Credenciales enviadas.")

            time.sleep(2)

            # Hover sobre el menú principal
            hover_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@onmouseover='popup(\"mainmenu\")']"))
            )
            actions = ActionChains(driver)
            actions.move_to_element(hover_element).perform()
            logging.info(f"Ventana {driver_number}: Hover realizado.")

            time.sleep(2)

            # Esperar y hacer clic en la opción del menú
            menu_opcion = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "el5"))
            )
            menu_opcion.click()
            logging.info(f"Ventana {driver_number}: Menú desplegado y opción seleccionada.")

            time.sleep(2)

            driver.execute_script("""
                window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
                });
            """)

            time.sleep(2)

            img_element = driver.find_element(By.NAME, "SearchSubCon")
            img_element.click()

            # Espera hasta que la ventana emergente se haya abierto
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Asegura que haya 2 ventanas abiertas

            # Obtén todas las ventanas abiertas
            windows = driver.window_handles

            # Cambia al contexto de la ventana emergente (la segunda ventana)
            driver.switch_to.window(windows[1])

            time.sleep(2)

            checkbox = driver.find_element(By.NAME, "chkItem5")
            checkbox.click()  # Esto marcará o desmarcará el checkbox

            time.sleep(2)

            aceptar_img = driver.find_element(By.NAME, "Criterio_r2_c1")
            aceptar_img.click()

            time.sleep(2)

            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))

            windows = driver.window_handles

            driver.switch_to.window(windows[0])

            time.sleep(2)

            driver.execute_script("""
                window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
                });
            """)

            time.sleep(2)

            generar_img = driver.find_element(By.NAME, "cmdGenerar")
            generar_img.click()

            windows = driver.window_handles

            driver.switch_to.window(windows[1])

            time.sleep(2)

            for i in range(1,35):
                cuadro = driver.find_element(By.NAME, f"no_paq_pzs_{i}")
                cuadro.send_keys(Keys.ARROW_RIGHT)
                cuadro.send_keys(Keys.BACKSPACE)
                time.sleep(1)
                random_number = random.randint(1,10)
                cuadro.send_keys(str(random_number))
                time.sleep(1)
        
            time.sleep(2)

            driver.execute_script("""
                window.scrollTo({
                top: 0,
                behavior:'smooth'
                });
            """)
        
            time.sleep(1)
        
            enviar_datos = driver.find_element(By.NAME, "btnInsert")
            enviar_datos.click()

        elif driver_number in [4,5,6]:

            # Esperar a los campos de usuario y contraseña
            username_field = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "txtUsuario"))
            )
            password_field = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "txtContrasena"))
            )
            logging.info(f"Ventana {driver_number}: Campos de login localizados.")

            time.sleep(2)

            username_field.send_keys("")
            password_field.send_keys("")
            password_field.send_keys(Keys.RETURN)
            logging.info(f"Ventana {driver_number}: Credenciales enviadas.")
        
            time.sleep(2)

                        # Hover sobre el menú principal
            hover_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@onmouseover='popup(\"mainmenu\")']"))
            )
            actions = ActionChains(driver)
            actions.move_to_element(hover_element).perform()
            logging.info(f"Ventana {driver_number}: Hover realizado.")

            time.sleep(2)

            # Esperar y hacer clic en la opción del menú
            menu_opcion = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "el5"))
            )
            menu_opcion.click()
            logging.info(f"Ventana {driver_number}: Menú desplegado y opción seleccionada.")

            time.sleep(2)

            driver.execute_script("""
                window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
                });
            """)

            time.sleep(2)

            img_element = driver.find_element(By.NAME, "SearchSubCon")
            img_element.click()

            # Espera hasta que la ventana emergente se haya abierto
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Asegura que haya 2 ventanas abiertas

            # Obtén todas las ventanas abiertas
            windows = driver.window_handles

            # Cambia al contexto de la ventana emergente (la segunda ventana)
            driver.switch_to.window(windows[1])

            time.sleep(2)

            checkbox = driver.find_element(By.NAME, "chkItem1")
            checkbox.click()  # Esto marcará o desmarcará el checkbox

            time.sleep(2)

            aceptar_img = driver.find_element(By.NAME, "Criterio_r2_c1")
            aceptar_img.click()

            time.sleep(2)

            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))

            windows = driver.window_handles

            driver.switch_to.window(windows[0])

            time.sleep(2)

            driver.execute_script("""
                window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
                });
            """)

            time.sleep(2)

            generar_img = driver.find_element(By.NAME, "cmdGenerar")
            generar_img.click()

            windows = driver.window_handles

            driver.switch_to.window(windows[1])

            time.sleep(2)

            for i in range(1,35):
                cuadro = driver.find_element(By.NAME, f"no_paq_pzs_{i}")
                cuadro.send_keys(Keys.ARROW_RIGHT)
                cuadro.send_keys(Keys.BACKSPACE)
                time.sleep(1)
                random_number = random.randint(1,10)
                cuadro.send_keys(str(random_number))
                time.sleep(1)
        
            time.sleep(2)

            driver.execute_script("""
                window.scrollTo({
                top: 0,
                behavior:'smooth'
                });
            """)
        
            time.sleep(1)
        
            enviar_datos = driver.find_element(By.NAME, "btnInsert")
            enviar_datos.click()

        else:
            logging.info(f"Ventana {driver_number}: Realizando acción genérica.")
            # Acciones genéricas para otras ventanas
            driver.execute_script(f"alert('Acción genérica en ventana {driver_number}');")

        time.sleep(80)

    except Exception as e:
        logging.error(f"Ventana {driver_number}: Error - {e}")
    return driver

with ThreadPoolExecutor(max_workers=6) as executor:
    futures = [executor.submit(open_and_login, i) for i in range(1, 7)]
    for future in futures:
        future.result()