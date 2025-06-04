 # ==============================
# Programa: Procesador de Pagos Automático
# Versión : 1.2
# Autor   : [Tu Nombre]
# Fecha   : Junio 2025
#
# Descripción:
# Este programa simula el procesamiento automático de pagos entre dos cuentas (token1 y token2)
# usando una lógica balanceada. Implementa patrones de diseño como Singleton, Chain of Responsibility
# e Iterator, y rota entre cuentas mientras haya saldo disponible.
# ==============================

VERSION_ANTERIOR = "1.0"
VERSION_1_2 = "1.2"

# ------------------- Versión Anterior -------------------

class TokenManagerSingletonV1:
    _instance = None
    _tokens = {
        "token1": "C598-ECF9-F0F7-881A",
        "token2": "C598-ECF9-F0F7-881B"
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_token(self, token_name):
        return self._tokens.get(token_name, "TOKEN_DESCONOCIDO")

class PaymentProcessorV1:
    def __init__(self, saldos, token_manager):
        self.saldos = saldos
        self.token_manager = token_manager

    def process_payment(self, monto, token_name):
        if self.saldos.get(token_name, 0) >= monto:
            self.saldos[token_name] -= monto
            token = self.token_manager.get_token(token_name)
            print(f"Versión {VERSION_ANTERIOR}: Pago de ${monto} con {token_name} (token: {token})")
            return True
        else:
            print(f"Versión {VERSION_ANTERIOR}: Saldo insuficiente en {token_name}")
            return False

def run_version_1_0():
    print(f"\n=== Ejecutando versión {VERSION_ANTERIOR} ===")
    saldos = {"token1": 1000, "token2": 2000}
    token_manager = TokenManagerSingletonV1()
    processor = PaymentProcessorV1(saldos, token_manager)

    pagos = [(500, "token1"), (1500, "token2"), (600, "token1")]
    for monto, token_name in pagos:
        processor.process_payment(monto, token_name)

    print(f"Saldos finales: {saldos}")

# ------------------- Versión 1.2 -------------------

class TokenManagerSingleton:
    _instance = None
    _tokens = {
        "token1": "C598-ECF9-F0F7-881A",
        "token2": "C598-ECF9-F0F7-881B"
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_token(self, token_name):
        return self._tokens.get(token_name, "TOKEN_DESCONOCIDO")

class CuentaHandler:
    def __init__(self, nombre, saldo, token_manager):
        self.nombre = nombre
        self.saldo = saldo
        self.token_manager = token_manager
        self.historial = []

    def puede_pagar(self, monto):
        return self.saldo >= monto

    def procesar_pago(self, monto, pedido_id):
        if not self.puede_pagar(monto):
            raise ValueError(f"{self.nombre} no tiene saldo suficiente.")
        self.saldo -= monto
        token = self.token_manager.get_token(self.nombre)
        print(f"Versión {VERSION_1_2}: Pedido #{pedido_id} - Pago de ${monto} con {self.nombre} (token {token})")
        self.historial.append((pedido_id, monto, self.nombre))

class HistorialIterator:
    def __init__(self, pagos):
        self._pagos = pagos
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._pagos):
            pago = self._pagos[self._index]
            self._index += 1
            return pago
        raise StopIteration

class ProcesadorPagos:
    def __init__(self, cuentas):
        self.cuentas = cuentas
        self.turno = 0
        self.pedido_actual = 1
        self.historial_global = []

    def procesar_pedido(self, monto):
        intentos = 0
        total_cuentas = len(self.cuentas)

        while intentos < total_cuentas:
            cuenta = self.cuentas[self.turno]
            if cuenta.puede_pagar(monto):
                cuenta.procesar_pago(monto, self.pedido_actual)
                self.historial_global.append((self.pedido_actual, cuenta.nombre, monto))
                self.pedido_actual += 1
                self.turno = (self.turno + 1) % total_cuentas
                return True
            else:
                print(f"Versión {VERSION_1_2}:  {cuenta.nombre} sin saldo para pedido #{self.pedido_actual}")
                self.turno = (self.turno + 1) % total_cuentas
                intentos += 1

        print(f"Versión {VERSION_1_2}:  Pedido #{self.pedido_actual} no procesado, sin saldo.")
        self.pedido_actual += 1
        return False

    def get_historial(self):
        return HistorialIterator(self.historial_global)

def run_version_1_2():
    print(f"\n=== Ejecutando versión {VERSION_1_2} ===")
    token_manager = TokenManagerSingleton()
    cuenta1 = CuentaHandler("token1", 1000, token_manager)
    cuenta2 = CuentaHandler("token2", 2000, token_manager)

    procesador = ProcesadorPagos([cuenta1, cuenta2])

    for _ in range(6):
        procesador.procesar_pedido(500)

    print("\nHistorial de pagos:")
    historial = procesador.get_historial()
    for pedido_id, cuenta, monto in historial:
        print(f"Pedido #{pedido_id}: ${monto} con {cuenta}")

    print("\nSaldos finales:")
    for cuenta in [cuenta1, cuenta2]:
        print(f"{cuenta.nombre}: ${cuenta.saldo}")

# ------------------- Bloque principal -------------------

if __name__ == "__main__":
    run_version_1_0()
    run_version_1_2()

def get_token(self, token_name):
    return self._tokens.get(token_name, "TOKEN_DESCONOCIDO")

def get_token(self, token_name):
    """
    Devuelve el token para el nombre dado.

    Args:
        token_name (str): Nombre del token.

    Returns:
        str: Token correspondiente o "TOKEN_DESCONOCIDO" si no existe.
    """
    return self._tokens.get(token_name, "TOKEN_DESCONOCIDO")
