from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env.local
load_dotenv()

def iniciar_sesion_factorial():
    # Ruta al Brave Browser en tu sistema
    browser_path = os.getenv("BROWSER_PATH")

    # Ruta al ChromeDriver descargado manualmente
    chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe")

    # Configurar opciones para Brave
    options = webdriver.ChromeOptions()
    options.binary_location = browser_path

    # Configurar el servicio con el ChromeDriver local
    service = Service(chromedriver_path)

    # Inicializar el driver
    driver = webdriver.Chrome(service=service, options=options)

    # URL de la página de registro de jornada
    url = "https://api.factorialhr.com/en/users/sign_in"

    # Abrir la página de inicio de sesión
    driver.get(url)

    # Esperar a que los campos de inicio de sesión estén presentes
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.presence_of_element_located((By.ID, "user_email")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "user_password")))

    # Obtener las credenciales de las variables de entorno
    email = os.getenv("FACTORIAL_EMAIL")
    password = os.getenv("FACTORIAL_PASSWORD")

    # Ingresar las credenciales
    email_field.send_keys(email)
    password_field.send_keys(password)

    # Esperar a que el formulario esté presente y enviarlo
    form = wait.until(EC.presence_of_element_located((By.ID, "new_user")))
    form.submit()

    return driver, wait
