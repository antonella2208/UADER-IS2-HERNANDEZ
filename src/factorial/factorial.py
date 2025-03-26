def factorial(n):
    """Calcula el factorial de un número entero positivo."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def calcular_factoriales(desde, hasta):
    """Calcula los factoriales de un rango de números."""
    for num in range(desde, hasta + 1):
        print(f"{num}! = {factorial(num)}")

# Solicitar el rango o número al usuario
rango = input("Ingrese un número o un rango (ejemplo: 4, 4-8, -10, 5-): ").strip()

try:
    if "-" in rango:
        partes = rango.split("-")

        # Caso "-hasta" → Calcula desde 1 hasta el número indicado
        if partes[0] == "":  
            desde = 1
            hasta = int(partes[1])

        # Caso "desde-" → Calcula desde el número indicado hasta 60
        elif partes[1] == "":
            desde = int(partes[0])
            hasta = 60

        # Caso "desde-hasta" → Calcula entre los dos valores indicados
        else:
            desde, hasta = map(int, partes)

    else:
        # Caso de un solo número → Calcula solo ese factorial
        desde = hasta = int(rango)

    # Validaciones
    if desde > hasta:
        print("Error: El primer número debe ser menor o igual al segundo.")
    elif desde < 0 or hasta < 0:
        print("Error: No se permiten números negativos.")
    elif hasta > 60:
        print("Error: No se pueden calcular factoriales mayores a 60 por su tamaño.")
    else:
        calcular_factoriales(desde, hasta)

except ValueError:
    print("Error: Ingrese un número válido o un rango .")
