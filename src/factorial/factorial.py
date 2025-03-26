#!/usr/bin/python
import sys

def factorial(n):
    """Calcula el factorial de un número entero positivo."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def calcular_factoriales(desde, hasta):
    """Calcula los factoriales de un rango de números."""
    for num in range(desde, hasta + 1):
        print(f"{num}! = {factorial(num)}")

# Solicitar el rango al usuario si no se pasa como argumento
rango = input("Ingrese un rango (ejemplo: 4-8): ").strip()

try:
    desde, hasta = map(int, rango.split("-"))  # Convertir entrada a enteros
    if desde > hasta:
        print("Error: El primer número debe ser menor o igual al segundo.")
    elif desde < 0 or hasta < 0:
        print("Error: No se permiten números negativos.")
    else:
        calcular_factoriales(desde, hasta)
except ValueError:
    print("Error: Ingrese un rango válido en el formato 'desde-hasta'.")

