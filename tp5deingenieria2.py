import os
class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content
        
class FileWriterCaretaker:
    def __init__(self):
        self.history = []

    def save(self, writer):
        memento = writer.save()
        if len(self.history) == 4:
            self.history.pop(0)  
        self.history.append(memento)

    def undo(self, writer, index):
        if index < 0 or index >= len(self.history):
            print(f"No hay un estado guardado en la posición {index}")
            return
        memento = self.history[-1 - index]
        writer.undo(memento)

if __name__ == '__main__':
    os.system("clear")

    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility("GFG.txt")

    print("Se escribe y guarda versión 1")
    writer.write("Versión 1\n")
    caretaker.save(writer)

    print("Se escribe y guarda versión 2")
    writer.write("Versión 2\n")
    caretaker.save(writer)

    print("Se escribe y guarda versión 3")
    writer.write("Versión 3\n")
    caretaker.save(writer)

    print("Se escribe y guarda versión 4")
    writer.write("Versión 4\n")
    caretaker.save(writer)

    print("Se escribe y guarda versión 5 (esto elimina la versión 1)")
    writer.write("Versión 5\n")
    caretaker.save(writer)

    print("\n--- Estado actual ---")
    print(writer.content)

    print("\n--- Undo(0): volver al último guardado ---")
    caretaker.undo(writer, 0)
    print(writer.content)

    print("\n--- Undo(2): volver a dos versiones atrás ---")
    caretaker.undo(writer, 2)
    print(writer.content)

    print("\n--- Undo(4): fuera de rango ---")
    caretaker.undo(writer, 4)

print()
import os

class State:
	def scan(self):
		if self.mode == 'stations':
			self.pos += 1
			if self.pos >= len(self.stations):
				self.pos = 0
				self.mode = 'memorias'
			print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))
		else:  
			self.mem_pos += 1
			if self.mem_pos >= len(self.memorias):
				self.mem_pos = 0
				self.mode = 'stations'
			print("Sintonizando... Memoria {} {}".format(self.memorias[self.mem_pos], self.name))

class AmState(State):
	def __init__(self, radio):
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.memorias = ["M1(1320)", "M2(1410)", "M3(1550)", "M4(1230)"]
		self.pos = -1
		self.mem_pos = -1
		self.mode = 'stations'
		self.name = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

class FmState(State):
	def __init__(self, radio):
		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.memorias = ["M1(88.9)", "M2(90.5)", "M3(95.7)", "M4(102.3)"]
		self.pos = -1
		self.mem_pos = -1
		self.mode = 'stations'
		self.name = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

class Radio:
	def __init__(self):
		self.fmstate = FmState(self)
		self.amstate = AmState(self)
		self.state = self.fmstate 

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		self.state.scan()

if __name__ == "__main__":
	os.system("clear")
	print("\nCrea un objeto radio y ejecuta acciones con estaciones y memorias")
	radio = Radio()
	actions = [radio.scan] * 7 + [radio.toggle_amfm] + [radio.scan] * 7
	actions *= 2

	print("\n Recorriendo acciones:")
	for action in actions:
		action()

print()
class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, number):
        if self.next_handler:
            return self.next_handler.handle(number)
        else:
            return f"{number} no consumido"

class PrimeHandler(Handler):
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            return f"{number} consumido por PrimeHandler"
        return super().handle(number)

class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            return f"{number} consumido por EvenHandler"
        return super().handle(number)

prime_handler = PrimeHandler()
even_handler = EvenHandler()

prime_handler.set_next(even_handler)

for i in range(1, 101):
    resultado = prime_handler.handle(i)
    print(resultado)

class StringIterable:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return ForwardIterator(self.text)

    def reverse_iterator(self):
        return ReverseIterator(self.text)

class ForwardIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        char = self.text[self.index]
        self.index += 1
        return char

print()

class ReverseIterator:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        char = self.text[self.index]
        self.index -= 1
        return char

cadena = StringIterable("Hola Mundo")

print("Recorrido directo:")
for c in cadena:
    print(c, end=" ")

print("\nRecorrido reverso:")
for c in cadena.reverse_iterator():
    print(c, end=" ")
    
print()

class EmisorID:
    def __init__(self):
        self.observers = []

    def suscribir(self, observer):
        self.observers.append(observer)

    def emitir_id(self, id_empleado):
        print(f"\n Emisor emite ID: {id_empleado}")
        for obs in self.observers:
            obs.notificar(id_empleado)

class Observer:
    def __init__(self, id_propio):
        self.id_propio = id_propio

    def notificar(self, id_empleado):
        if id_empleado == self.id_propio:
            print(f" Coincidencia: {self.__class__.__name__} reaccionó al ID '{id_empleado}'")

class ClaseA(Observer):
    def __init__(self):
        super().__init__("AB12")

class ClaseB(Observer):
    def __init__(self):
        super().__init__("CD34")

class ClaseC(Observer):
    def __init__(self):
        super().__init__("EF56")

class ClaseD(Observer):
    def __init__(self):
        super().__init__("GH78")

emisor = EmisorID()
obs_a = ClaseA()
obs_b = ClaseB()
obs_c = ClaseC()
obs_d = ClaseD()

emisor.suscribir(obs_a)
emisor.suscribir(obs_b)
emisor.suscribir(obs_c)
emisor.suscribir(obs_d)

ids_a_emitir = ["ZZ99", "AB12", "1234", "CD34", "0000", "EF56", "9999", "GH78"]

for id_actual in ids_a_emitir:
    emisor.emitir_id(id_actual)
    
