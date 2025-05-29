
# ------------------------------------------------------------------------------
# getjson.py
#
# Copyright UADER-FCyT-IS2 © 2024 - Todos los derechos reservados.
# Este programa es propiedad de la Universidad Autónoma de Entre Ríos,
# Facultad de Ciencia y Tecnología - Ingeniería en Software II.
#
# Descripción:
# Programa que lee un valor desde un archivo Python (sitedata.py) que contiene
# un diccionario con claves y valores. Usa el patrón Singleton y una interfaz
# de abstracción. Diseñado para evitar errores del sistema y manejar fallos de
# forma controlada.
# ------------------------------------------------------------------------------

import os
import importlib.util
import json
from abc import ABC, abstractmethod

class IReader(ABC):
    @abstractmethod
    def get_value(self, key):
        pass

class JSONReader(IReader):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JSONReader, cls).__new__(cls)
            cls._instance._load_data()
        return cls._instance

    def _load_data(self):
        try:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            path = os.path.join(base_dir, "assets", "config", "sitedata.py")

            if not os.path.isfile(path):
                print(f"[ERROR] No se encontró el archivo: {path}")
                self._data = {}
                return

            spec = importlib.util.spec_from_file_location("sitedata", path)
            sitedata = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(sitedata)

            if hasattr(sitedata, "data") and isinstance(sitedata.data, dict):
                self._data = sitedata.data
            else:
                print("[ERROR] 'sitedata.py' no contiene un diccionario llamado 'data'.")
                self._data = {}

        except Exception as e:
            print(f"[ERROR] Falló la carga de sitedata.py: {e}")
            self._data = {}

    def get_value(self, key):
        return self._data.get(key, None)

class LegacyReader(IReader):
    def __init__(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self._file_path = os.path.join(base_dir, "assets", "config", "sitedata.json")

    def get_value(self, key):
        try:
            with open(self._file_path, "r") as f:
                data = json.load(f)
            return data.get(key, f"[ERROR] Clave '{key}' no encontrada.")
        except Exception as e:
            return f"[ERROR] {e}"

import sys

class App:
    def __init__(self, key="token1", legacy=False):
        self.reader = LegacyReader() if legacy else JSONReader()
        self.key = key

    def run(self):
        value = self.reader.get_value(self.key)
        if value:
            print(f"✔ Valor de '{self.key}': {value}")
        else:
            print(f"[ERROR] La clave '{self.key}' no existe.")

if __name__ == "__main__":
    try:
        legacy = "--legacy" in sys.argv
        args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
        key = args[0] if args else "token1"

        app = App(key, legacy)
        app.run()
    except Exception as e:
        print(f"[ERROR] Fallo inesperado: {e}")
        sys.exit(1)

import sys
class App:
    def __init__(self, key="token1", legacy=False):
        self.reader = LegacyReader() if legacy else JSONReader()
        self.key = key

    def run(self):
        value = self.reader.get_value(self.key)
        if value:
            print(f"✔ Valor de '{self.key}': {value}")
        else:
            print(f"[ERROR] La clave '{self.key}' no existe.")

def mostrar_ayuda():
    print("""
Uso: python getjson.py <clave> [--legacy]

<clave>        Clave a buscar (opcional, por defecto 'token1')
--legacy       Utiliza el lector JSON antiguo (sitedata.json)
--help         Muestra este mensaje de ayuda
""")

if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        if "--help" in args:
            mostrar_ayuda()
            sys.exit(0)

        legacy = "--legacy" in args
        args = [arg for arg in args if not arg.startswith("--")]

        if len(args) > 1:
            print("[ERROR] Demasiados argumentos.")
            mostrar_ayuda()
            sys.exit(1)

        key = args[0] if args else "token1"

        app = App(key, legacy)
        app.run()

    except Exception as e:
        print(f"[ERROR] Fallo inesperado: {e}")
        sys.exit(1)

import sys

VERSION = "1.1"

class App:
    def __init__(self, key="token1", legacy=False):
        self.reader = LegacyReader() if legacy else JSONReader()
        self.key = key

    def run(self):
        value = self.reader.get_value(self.key)
        if value:
            print(f"✔ Valor de '{self.key}': {value}")
        else:
            print(f"[ERROR] La clave '{self.key}' no existe.")

def mostrar_ayuda():
    print(f"""
Uso: python getjson.py <clave> [--legacy]

<clave>        Clave a buscar (opcional, por defecto 'token1')
--legacy       Utiliza el lector JSON antiguo (sitedata.json)
-v             Muestra la versión del programa
--help         Muestra este mensaje de ayuda
""")

if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        if "-v" in args:
            print(f"Versión {VERSION}")
            sys.exit(0)

        if "--help" in args:
            mostrar_ayuda()
            sys.exit(0)

        legacy = "--legacy" in args
        args = [arg for arg in args if not arg.startswith("--") and arg != "-v"]

        if len(args) > 1:
            print("[ERROR] Demasiados argumentos.")
            mostrar_ayuda()
            sys.exit(1)

        key = args[0] if args else "token1"

        app = App(key, legacy)
        app.run()

    except Exception as e:
        print(f"[ERROR] Fallo inesperado: {e}")
        sys.exit(1)

# getjson.py
# Copyright UADER-FCyT-IS2 © 2024 - Todos los derechos reservados.
"""
Módulo principal que permite obtener un valor desde un archivo de configuración
utilizando un patrón Singleton. Incluye soporte para versiones legacy y abstracción por interfaz.
"""

import sys
VERSION = "1.1"

class App:
    """Clase principal que ejecuta la lógica de lectura usando un lector."""

    def __init__(self, key="token1", legacy=False):
        self.reader = LegacyReader() if legacy else JSONReader()
        self.key = key

    def run(self):
        """Ejecuta la lectura de clave y muestra el valor asociado."""
        value = self.reader.get_value(self.key)
        if value:
            print(f"✔ Valor de '{self.key}': {value}")
        else:
            print(f"[ERROR] La clave '{self.key}' no existe.")

def mostrar_ayuda():
    """Muestra un mensaje de ayuda para el uso por línea de comandos."""
    print(f"""
Uso: python getjson.py <clave> [--legacy]

<clave>        Clave a buscar (opcional, por defecto 'token1')
--legacy       Utiliza el lector JSON antiguo (sitedata.json)
-v             Muestra la versión del programa
--help         Muestra este mensaje de ayuda
""")

def main():
    """Punto de entrada principal del script"""
    try:
        args = sys.argv[1:]

        if "-v" in args:
            print(f"Versión {VERSION}")
            sys.exit(0)

        if "--help" in args:
            mostrar_ayuda()
            sys.exit(0)

        legacy = "--legacy" in args
        args = [arg for arg in args if not arg.startswith("--") and arg != "-v"]

        if len(args) > 1:
            print("[ERROR] Demasiados argumentos.")
            mostrar_ayuda()
            sys.exit(1)

        key = args[0] if args else "token1"

        app = App(key, legacy)
        app.run()

    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"[ERROR] Fallo inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
