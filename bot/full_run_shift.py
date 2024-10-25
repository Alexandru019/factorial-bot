import time
import subprocess
from datetime import datetime

# Obtener el día actual de la semana (0 es lunes, 4 es viernes)
dia_actual = datetime.now().weekday()

# Ejecutar el script de inicio de jornada
subprocess.run(["python", "bot/start_shift.py"])

if dia_actual == 4:  # Si es viernes
    # Esperar 6 horas (6 * 60 * 60 segundos)
    time.sleep(6 * 60 * 60)
    
    # Ejecutar el script de fin de jornada
    subprocess.run(["python", "bot/end_shift.py"])
else:
    # Esperar 6 horas (6 * 60 * 60 segundos)
    time.sleep(6 * 60 * 60)

    # Ejecutar el script de pausa de jornada
    subprocess.run(["python", "bot/pause_shift.py"])

    # Esperar 1 hora (1 * 60 * 60 segundos)
    time.sleep(1 * 60 * 60)

    # Ejecutar el script de reanudación de jornada
    subprocess.run(["python", "bot/resume_shift.py"])

    # Esperar 2 horas y media (2.5 * 60 * 60 segundos)
    time.sleep(2.5 * 60 * 60)

    # Ejecutar el script de fin de jornada
    subprocess.run(["python", "bot/end_shift.py"])
