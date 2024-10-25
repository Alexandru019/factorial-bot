import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from factorial_utils import iniciar_sesion_factorial

# Iniciar sesión y obtener el driver y wait
driver, wait = iniciar_sesion_factorial()

# Esperar a que cargue el dashboard o página principal
time.sleep(10)  # Esperamos 10 segundos para asegurarnos de que la página cargue completamente

# Intentar encontrar el botón de parar con diferentes selectores
selectors = [
    "//button[.//use[contains(@href, '#stop')]]",
    "//button[contains(@class, 'tether-target')]",
    "//button[.//svg[contains(@class, '_1qphaha')]]",
    "//button[contains(@class, '_1nz7aia')]"
]

for selector in selectors:
    try:
        stop_button = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
        print(f"Botón encontrado con selector: {selector}")
        stop_button.click()
        print("Botón clickeado exitosamente")
        break
    except Exception as e:
        print(f"No se pudo encontrar el botón con el selector: {selector}")
        print(f"Error: {str(e)}")


# Cerrar el navegador
driver.quit()
