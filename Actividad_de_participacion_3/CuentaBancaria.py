class CuentaBancaria:
    def __init__(self, propietarios=["Laura Martinez", "Sara Castro"]):
        self.numero_cuenta = 258496532
        self.propietarios = propietarios
        self.__balance = 50000

    def depositar(self, monto):
        if monto > 0:
            self.__balance += monto
            print(f"Se ha depositado ${monto} en la cuenta {self.numero_cuenta}. Saldo actual: ${self.__balance:.2f}")
        else:
            print("No se puede depositar un monto negativo o cero.")

    def imprimir_datos(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Saldo actual: ${self.__balance:.2f}")

cuenta = CuentaBancaria()
cuenta.imprimir_datos()


cuenta.depositar(1000000)

cuenta.imprimir_datos()