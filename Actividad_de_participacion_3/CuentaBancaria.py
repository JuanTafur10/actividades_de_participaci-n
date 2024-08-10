class CuentaBancaria:
    def __init__(self, propietarios=["Laura Martinez", "Sara Castro"]):
        self.numero_cuenta = 258496532
        self.propietarios = propietarios
        self.__balance = 2000

    def depositar(self, monto):
        if monto > 0:
            self.__balance += monto
            print(f"Se ha depositado ${monto} en la cuenta {self.numero_cuenta}. Saldo actual: ${self.__balance:.2f}")
        else:
            print("No se puede depositar un monto negativo o cero.")

    def retirar(self, monto):
        if monto > 0 and monto <= self.__balance:
            self.__balance -= monto
            print(f"Se ha retirado ${monto} de la cuenta {self.numero_cuenta}. Saldo actual: ${self.__balance:.2f}")
        elif monto > self.__balance:
            print(f"No se puede retirar ${monto} de la cuenta, ya que el saldo actual es solo ${self.__balance:.2f}.")
        else:
            print("No se puede retirar un monto negativo o cero.")

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.__balance * 0.02
        self.__balance -= cuota_manejo
        print(f"Se ha aplicado una cuota de manejo del 2% sobre la cuenta {self.numero_cuenta}. Cuota: ${cuota_manejo:.2f}. Saldo actual: ${self.__balance:.2f}")


    def imprimir_datos(self):
        print(f"Saldo actual: ${self.__balance:.2f}")

    def mostrar_detalles(self):
        print("Detalles de la cuenta bancaria:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Saldo actual: ${self.__balance:.2f}")

cuenta = CuentaBancaria()
cuenta.imprimir_datos()


cuenta.depositar(50000)
cuenta.imprimir_datos()


cuenta.aplicar_cuota_manejo()

cuenta.retirar(30000)
print(f"Saldo actual: ${cuenta._CuentaBancaria__balance:.2f}")

cuenta.mostrar_detalles()

