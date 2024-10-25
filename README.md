# Factorial HR Bot

Factorial HR Bot es una herramienta automatizada diseñada para interactuar con la plataforma Factorial HR. Este bot facilita la tarea rutinaria de registro de horas de trabajo.

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)
- Node.js y npm (para usar `npx`)
- Navegador basado en Chromium (como Google Chrome)
- Versión compatible de ChromeDriver

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/Alexandru019/factorial-hr-bot.git
   cd factorial-hr-bot
   ```

2. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Instala Node.js y npm:**

   Si aún no tienes `Node.js` y `npm` instalados, descárgalos e instálalos desde [nodejs.org](https://nodejs.org/).

4. **Configura las credenciales:**

   Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido:

   ```
   FACTORIAL_EMAIL="tu_correo"
   FACTORIAL_PASSWORD="tu_contraseña"
   BROWSER_PATH="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
   ```

   Asegúrate de reemplazar `tu_correo` y `tu_contraseña` con tus credenciales reales y `BROWSER_PATH` con la ruta correcta a tu navegador.

5. **Instala la versión correcta de ChromeDriver:**

   Verifica la versión de tu navegador y asegúrate de instalar una versión de ChromeDriver que sea igual o inferior a la versión de tu navegador, pero nunca superior. Usa el siguiente comando para instalar ChromeDriver:

   ```bash
   npx @puppeteer/browsers install chromedriver@130.0.6723.58
   ```

   Reemplaza `130.0.6723.58` con la versión adecuada para tu navegador.

6. **Coloca `chromedriver.exe` en la raíz del proyecto:**

   Una vez descargado, asegúrate de que el archivo `chromedriver.exe` esté ubicado en la raíz del proyecto, junto al archivo `.env`.


7. **Crea un archivo `.bat` para ejecutar el bot:**

   Crea un archivo llamado `ejecutar_bot.bat` en la raíz del proyecto con el siguiente contenido:

   ```batch
   @echo off
   python bot\full_run_shift.py
   pause
   ```

## Uso

Para ejecutar el bot, simplemente haz doble clic en el archivo `ejecutar_bot.bat`. Esto abrirá una ventana de comandos y ejecutará el script automáticamente.

## Notas

- Este bot actualmente solo está preparado para navegadores basados en Chromium y no es compatible con Firefox.
- Asegúrate de que el archivo `.env` no se suba al repositorio. Está incluido en el archivo `.gitignore` por defecto.


## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
