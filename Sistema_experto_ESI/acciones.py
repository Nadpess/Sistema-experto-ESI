"""
Interfaz de consola y funciones de manejo de la base de conocimientos
"""
from experto_general.engine import Engine

# Motor como variable global
engine = Engine()

try:
    archivo = "ESI.json"
    engine.base.from_json(archivo)
    print(f"Base de conocimientos {archivo} cargada exitosamente.")
except Exception as e:
    print(f"Error al cargar la base de conocimientos: {e}")
