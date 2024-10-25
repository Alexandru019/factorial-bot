import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from factorial_utils import iniciar_sesion_factorial

# Iniciar sesión y obtener el driver y wait
driver, wait = iniciar_sesion_factorial()

# Esperar a que cargue el dashboard o página principal
time.sleep(10)

# Marcar el inicio de la jornada laboral
fichar_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Fichar')]]")))
fichar_button.click()

# Cerrar el navegador
driver.quit()
