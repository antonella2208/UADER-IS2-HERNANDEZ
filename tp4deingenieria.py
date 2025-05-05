
import os
import platform

class Ping:
    def execute(self, ip: str):
        if not ip.startswith("192."):
            raise ValueError("Dirección IP no permitida. Debe comenzar con '192.'")
        self._ping(ip)

    def executefree(self, ip: str):
        self._ping(ip)

    def _ping(self, ip: str):
        print(f"Haciendo ping a {ip} (10 intentos)...")
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        os.system(f"ping {param} 10 {ip}")

class PingProxy:
    def __init__(self):
        self._ping = Ping()

    def execute(self, ip: str):
        if ip == "192.168.0.254":
            print("Redirigiendo ping a www.google.com (vía executefree)...")
            self._ping.executefree("www.google.com")
        else:
            print(f"Usando ping con restricción para IP: {ip}")
            self._ping.execute(ip)


if __name__ == "__main__":
    proxy = PingProxy()

    try:
        proxy.execute("192.168.0.10")       
        proxy.execute("192.168.0.254")      
        proxy.execute("10.0.0.1")           
    except ValueError as e:
        print(f"Error: {e}")
        
print()        
from abc import ABC, abstractmethod
class TrenLaminador(ABC):
    @abstractmethod
    def laminar(self, lamina):
        pass

class TrenLaminador5m(TrenLaminador):
    def laminar(self, lamina):
        print(f"Produciendo lámina de {lamina.ancho}m x 5m x {lamina.espesor}\" en Tren Laminador de 5 metros.")

class TrenLaminador10m(TrenLaminador):
    def laminar(self, lamina):
        print(f"Produciendo lámina de {lamina.ancho}m x 10m x {lamina.espesor}\" en Tren Laminador de 10 metros.")

class Lamina:
    def __init__(self, espesor: float, ancho: float, tren: TrenLaminador):
        self.espesor = espesor
        self.ancho = ancho
        self.tren = tren

    def producir(self):
        self.tren.laminar(self)

if __name__ == "__main__":
    tren5 = TrenLaminador5m()
    tren10 = TrenLaminador10m()

    lamina1 = Lamina(0.5, 1.5, tren5)
    lamina2 = Lamina(0.5, 1.5, tren10)

    lamina1.producir()  
    lamina2.producir()  
   
print()
from abc import ABC, abstractmethod

class Componente(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass

class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Pieza: {self.nombre}")

class Ensamblado(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente: Componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Ensamblado: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)

producto_principal = Ensamblado("Producto Principal")

for i in range(1, 4):
    subconjunto = Ensamblado(f"Subconjunto {i}")
    for j in range(1, 5):
        pieza = Pieza(f"Pieza {i}.{j}")
        subconjunto.agregar(pieza)
    producto_principal.agregar(subconjunto)

print("=== Estructura inicial ===")
producto_principal.mostrar()

subconjunto_extra = Ensamblado("Subconjunto Opcional")
for j in range(1, 5):
    subconjunto_extra.agregar(Pieza(f"Pieza Extra.{j}"))

producto_principal.agregar(subconjunto_extra)

print("\n=== Estructura con subconjunto opcional ===")
producto_principal.mostrar()   

print()

from abc import ABC, abstractmethod

class Numero(ABC):
    @abstractmethod
    def valor(self):
        pass

class NumeroBase(Numero):
    def __init__(self, numero):
        self._numero = numero

    def valor(self):
        return self._numero

class OperacionDecorator(Numero):
    def __init__(self, numero: Numero):
        self._numero = numero

class Sumar2(OperacionDecorator):
    def valor(self):
        return self._numero.valor() + 2

class Multiplicar2(OperacionDecorator):
    def valor(self):
        return self._numero.valor() * 2

class Dividir3(OperacionDecorator):
    def valor(self):
        return self._numero.valor() / 3

if __name__ == "__main__":
    numero_original = NumeroBase(9)
    print("Número original:", numero_original.valor())

    decorado1 = Sumar2(numero_original)
    print("Después de sumar 2:", decorado1.valor())

    decorado2 = Multiplicar2(decorado1)
    print("Después de multiplicar por 2:", decorado2.valor())

    decorado3 = Dividir3(decorado2)
    print("Después de dividir por 3:", decorado3.valor())

    resultado_final = Dividir3(Multiplicar2(Sumar2(NumeroBase(9))))
    print("Resultado con operaciones anidadas directamente:", resultado_final.valor())
 
print()   

from abc import ABC, abstractmethod

class LaminaFlyweight:
    def __init__(self, espesor: float, ancho: float):
        self.espesor = espesor
        self.ancho = ancho

    def mostrar(self, longitud, tren_nombre):
        print(f"Lámina de {self.ancho}m x {longitud}m x {self.espesor}\" usando {tren_nombre}")

class LaminaFactory:
    _laminas = {}

    @staticmethod
    def get_lamina(espesor: float, ancho: float):
        key = (espesor, ancho)
        if key not in LaminaFactory._laminas:
            LaminaFactory._laminas[key] = LaminaFlyweight(espesor, ancho)
        return LaminaFactory._laminas[key]

class TrenLaminador(ABC):
    @abstractmethod
    def laminar(self, lamina: LaminaFlyweight, longitud: int):
        pass

class TrenLaminador5m(TrenLaminador):
    def laminar(self, lamina: LaminaFlyweight, longitud: int = 5):
        lamina.mostrar(longitud, "Tren Laminador 5m")

class TrenLaminador10m(TrenLaminador):
    def laminar(self, lamina: LaminaFlyweight, longitud: int = 10):
        lamina.mostrar(longitud, "Tren Laminador 10m")

if __name__ == "__main__":
    tren5 = TrenLaminador5m()
    tren10 = TrenLaminador10m()

    for i in range(5):
        lamina = LaminaFactory.get_lamina(0.5, 1.5)
        if i % 2 == 0:
            tren5.laminar(lamina)
        else:
            tren10.laminar(lamina)