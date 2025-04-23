class Factorial:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Factorial, cls).__new__(cls)
        return cls._instance

    def calcular(self, n):
        if not isinstance(n, int):
            raise TypeError("Debe ser un número entero.")
        if n < 0:
            raise ValueError("No se puede calcular el factorial de un número negativo.")

        resultado = 1
        for i in range(2, n + 1):
            resultado *= i

        return resultado


if __name__ == "__main__":
    while True:
        try:
            entrada = input("Introduce un número entero (o 'salir' para terminar): ")
            if entrada.lower() == "salir":
                break

            numero = int(entrada)
            factorial = Factorial()
            resultado = factorial.calcular(numero)
            print(f"El factorial de {numero} es {resultado}\n")

        except ValueError as ve:
            print(f"Error: {ve}\n")
        except TypeError as te:
            print(f"Error: {te}\n")

print()

class CalculadoraImpuestos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instance

    def calcular_total_impuestos(self, base_imponible):
        if not isinstance(base_imponible, (int, float)) or base_imponible < 0:
            raise ValueError("La base imponible debe ser un número positivo.")

        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012

        total_impuestos = iva + iibb + contribuciones
        return total_impuestos
    
if __name__ == "__main__":
    base = float(input("Ingrese la base imponible: "))
    calculadora = CalculadoraImpuestos()
    total = calculadora.calcular_total_impuestos(base)
    print(f"Total de impuestos sobre ${base:.2f} es ${total:.2f}")

print()

class ComidaRapida:
    def __init__(self, nombre):
        self.nombre = nombre

    def entregar_en_mostrador(self):
        print(f"{self.nombre} entregada en mostrador.")

    def retirar_por_cliente(self):
        print(f"{self.nombre} retirada por el cliente.")

    def enviar_por_delivery(self):
        print(f"{self.nombre} enviada por delivery.")


def mostrar_menu_comidas():
    print("Elija una comida:")
    print("1 - Hamburguesa")
    print("2 - Papas Fritas")
    print("3 - Pizza")


def mostrar_menu_entrega():
    print("Elija el método de entrega:")
    print("1 - Entregar en mostrador")
    print("2 - Retirar por el cliente")
    print("3 - Enviar por delivery")


if __name__ == "__main__":
    mostrar_menu_comidas()
    opcion_comida = input("Ingrese una opción: ")

    if opcion_comida == "1":
        comida = ComidaRapida("Hamburguesa")
    elif opcion_comida == "2":
        comida = ComidaRapida("Papas Fritas")
    elif opcion_comida == "3":
        comida = ComidaRapida("Pizza")
    else:
        print("Opción inválida de comida.")
        exit()

    mostrar_menu_entrega()
    opcion_entrega = input("Ingrese una opción: ")

    print()  # Salto de línea para mejor presentación

    if opcion_entrega == "1":
        comida.entregar_en_mostrador()
    elif opcion_entrega == "2":
        comida.retirar_por_cliente()
    elif opcion_entrega == "3":
        comida.enviar_por_delivery()
    else:
        print("Opción inválida de entrega.")
 
print()        

class Factura:
    def __init__(self, importe):
        self.importe = importe
        self.condicion_impositiva = self.determinar_condicion()

    def determinar_condicion(self):
        if self.importe < 1000:
            return "IVA Exento"
        elif 1000 <= self.importe <= 5000:
            return "IVA No Inscripto"
        else:
            return "IVA Responsable"

    def mostrar_factura(self):
        print("\n----- FACTURA -----")
        print(f"Importe total: ${self.importe:.2f}")
        print(f"Condición impositiva del cliente: {self.condicion_impositiva}")
        print("--------------------")


if __name__ == "__main__":
    try:
        importe = float(input("Ingrese el total de la factura: "))
        factura = Factura(importe)
        factura.mostrar_factura()
    except ValueError:
        print("Debe ingresar un número válido para el importe.")
        
print()

class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar_partes(self):
        print("\n✈️ Avión construido con las siguientes partes:")
        for parte in self.partes:
            print(f" - {parte}")

class ConstructorAvion:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        self.avion.agregar_parte("Cuerpo (Body)")

    def construir_turbinas(self):
        self.avion.agregar_parte("Turbina izquierda")
        self.avion.agregar_parte("Turbina derecha")

    def construir_alas(self):
        self.avion.agregar_parte("Ala izquierda")
        self.avion.agregar_parte("Ala derecha")

    def construir_tren_de_aterrizaje(self):
        self.avion.agregar_parte("Tren de aterrizaje")

    def obtener_avion(self):
        return self.avion

class DirectorAvion:
    def __init__(self, constructor):
        self.constructor = constructor

    def construir_avion_completo(self):
        self.constructor.construir_body()
        self.constructor.construir_turbinas()
        self.constructor.construir_alas()
        self.constructor.construir_tren_de_aterrizaje()
        return self.constructor.obtener_avion()

if __name__ == "__main__":
    constructor = ConstructorAvion()
    director = DirectorAvion(constructor)

    avion = director.construir_avion_completo()
    avion.mostrar_partes()
    
import copy

# Clase base que implementa el patrón Prototipo
class Prototipo:
    def clonar(self):
        return copy.deepcopy(self)

class Avion(Prototipo):
    def __init__(self, modelo, capacidad):
        self.modelo = modelo
        self.capacidad = capacidad

    def __str__(self):
        return f"Avión modelo {self.modelo} con capacidad para {self.capacidad} pasajeros"

if __name__ == "__main__":
    original = Avion("Boeing 737", 180)
    copia1 = original.clonar()  # Clon del original
    copia2 = copia1.clonar()    # Clon del clon

    print("Original:", original)
    print("Copia 1:", copia1)
    print("Copia 2:", copia2)

    print("\n¿Copia1 es un clon del original?", copia1 is not original)
    print("¿Copia2 es un clon de copia1?", copia2 is not copia1)

class Body:
    def crear(self):
        pass

class Ala:
    def crear(self):
        pass

class Turbina:
    def crear(self):
        pass
    
class FabricaAbstractaAvion:
    def crear_body(self):
        pass

    def crear_ala(self):
        pass

    def crear_turbina(self):
        pass

# Fábrica concreta para un avión comercial
class FabricaAvionComercial(FabricaAbstractaAvion):
    def crear_body(self):
        return BodyComercial()

    def crear_ala(self):
        return AlaComercial()

    def crear_turbina(self):
        return TurbinaComercial()

# Fábrica concreta para un avión privado
class FabricaAvionPrivado(FabricaAbstractaAvion):
    def crear_body(self):
        return BodyPrivado()

    def crear_ala(self):
        return AlaPrivada()

    def crear_turbina(self):
        return TurbinaPrivada()

class BodyComercial(Body):
    def crear(self):
        return "Cuerpo de avión comercial"

class BodyPrivado(Body):
    def crear(self):
        return "Cuerpo de avión privado"

class AlaComercial(Ala):
    def crear(self):
        return "Ala de avión comercial"

class AlaPrivada(Ala):
    def crear(self):
        return "Ala de avión privado"

class TurbinaComercial(Turbina):
    def crear(self):
        return "Turbina de avión comercial"

class TurbinaPrivada(Turbina):
    def crear(self):
        return "Turbina de avión privado"

class Avion:
    def __init__(self, fabrica):
        self.body = fabrica.crear_body()
        self.ala = fabrica.crear_ala()
        self.turbina = fabrica.crear_turbina()

    def mostrar_avion(self):
        print(f"Avión construido con: {self.body}, {self.ala}, {self.turbina}")

if __name__ == "__main__":
    tipo_avion = input("Seleccione el tipo de avión (comercial/privado): ").lower()

    if tipo_avion == "comercial":
        fabrica = FabricaAvionComercial()
    elif tipo_avion == "privado":
        fabrica = FabricaAvionPrivado()
    else:
        print("Tipo de avión no válido")
        exit()

    avion = Avion(fabrica)
    avion.mostrar_avion()

