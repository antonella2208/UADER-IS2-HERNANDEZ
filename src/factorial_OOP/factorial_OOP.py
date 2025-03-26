class Factorial:
    """Clase para calcular factoriales en un rango dado."""

    def __init__(self):
        """Constructor vacío, ya que no necesitamos inicializar variables de instancia."""
        pass

    def calcular(self, n):
        """Calcula el factorial de un número entero positivo."""
        if n == 0 or n == 1:
            return 1
        return n * self.calcular(n - 1)

    def run(self, min, max):
        """Calcula los factoriales entre min y max e imprime los resultados."""
        if min > max:
            print("Error: El primer número debe ser menor o igual al segundo.")
            return
        elif min < 0 or max < 0:
            print("Error: No se permiten números negativos.")
            return
        elif max > 60:
            print("Error: No se pueden calcular factoriales mayores a 60 por su tamaño.")
            return

        for num in range(min, max + 1):
            print(f"{num}! = {self.calcular(num)}")

rango = input("Ingrese un número o un rango (ejemplo: 4, 4-8, -10, 5-): ").strip()

try:
    if "-" in rango:
        partes = rango.split("-")

        if partes[0] == "":  
            min_val = 1
            max_val = int(partes[1])

        elif partes[1] == "":
            min_val = int(partes[0])
            max_val = 60

        else:
            min_val, max_val = map(int, partes)

    else:

        min_val = max_val = int(rango)

    fact = Factorial()
    fact.run(min_val, max_val)

except ValueError:
    print("Error: Ingrese un número válido o un rango en el formato .")
