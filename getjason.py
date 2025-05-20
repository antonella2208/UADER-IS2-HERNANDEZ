
import json
import sys

def main():
    key = "token1"
    if len(sys.argv) > 1:
        key = sys.argv[1]

    try:
        with open("sitedata.json", "r") as f:
            data = json.load(f)

        if key in data:
            print(data[key])
        else:
            print(f" La clave '{key}' no se encontró en sitedata.json.")

    except FileNotFoundError:
        print(" El archivo 'sitedata.json' no se encuentra en el directorio actual.")
    except json.JSONDecodeError:
        print(" Error al interpretar el archivo JSON (¿está mal formado?).")
    except Exception as e:
        print(f" Error inesperado: {e}")

if __name__ == "__main__":
    main()

import sys
import json

# Nombre del archivo JSON con las claves y tokens
FILENAME = "sitedata.json"

def obtener_valor(clave="token1"):
    """
    Recupera el valor de una clave específica desde el archivo JSON sitedata.json.
    Si no se proporciona una clave, se usa 'token1' por defecto.

    Parámetros:
        clave (str): La clave que se desea recuperar

    Retorna:
        str: El valor correspondiente a la clave solicitada

    Lanza:
        KeyError: Si la clave no existe en el JSON
        FileNotFoundError: Si el archivo no existe
        json.JSONDecodeError: Si el archivo JSON está mal formado
    """
    with open(FILENAME, "r") as archivo:
        datos = json.load(archivo)
    return datos[clave]

if __name__ == "__main__":
    # Obtener la clave desde la línea de comandos, o usar 'token1' como valor por defecto
    clave_solicitada = sys.argv[1] if len(sys.argv) > 1 else "token1"

    try:
        valor = obtener_valor(clave_solicitada)
        print(f"Valor de '{clave_solicitada}': {valor}")
    except FileNotFoundError:
        print(f"Error: El archivo {FILENAME} no se encuentra.")
    except KeyError:
        print(f"Error: La clave '{clave_solicitada}' no existe en el archivo.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON está mal formado.")

