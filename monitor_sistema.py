"""
Módulo monitor_sistema.py
Chequeo básico de salud del equipo/servidor: uso de CPU, memoria y disco.
Simula el tipo de diagnóstico rápido que se haría al asistir un puesto
de trabajo o servidor. Usa psutil; si no está instalado, avisa cómo
instalarlo en vez de romper el programa.
"""

try:
    import psutil
    PSUTIL_DISPONIBLE = True
except ImportError:
    PSUTIL_DISPONIBLE = False

UMBRAL_ALERTA = 85  # porcentaje


def chequear_salud():
    """Devuelve un diccionario con el uso de CPU/memoria/disco y alertas si corresponde."""
    if not PSUTIL_DISPONIBLE:
        return {
            "error": "El módulo 'psutil' no está instalado. Instalalo corriendo lo siguiente en tu terminal: py -m pip install -r requirements.txt"
        }

    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory().percent
    disco = psutil.disk_usage("/").percent

    resultado = {
        "cpu_percent": cpu,
        "memoria_percent": memoria,
        "disco_percent": disco,
        "alertas": [],
    }

    if cpu > UMBRAL_ALERTA:
        resultado["alertas"].append(f"Uso de CPU alto: {cpu}%")
    if memoria > UMBRAL_ALERTA:
        resultado["alertas"].append(f"Uso de memoria alto: {memoria}%")
    if disco > UMBRAL_ALERTA:
        resultado["alertas"].append(f"Uso de disco alto: {disco}%")

    return resultado
