import sys
from typing import Optional

from blackjack.model.blackjack import Blackjack


class UIConsola:

    def __init__(self):
        self.blackjack: Blackjack = Blackjack()
        self.opciones = {
            "1": self.iniciar_nuevo_juego,
            "2": self.salir
        }

    @staticmethod
    def mostrar_menu():
        titulo = "BLACKJACK"
        print(f"\n{titulo:_^30}")
        print("1. Iniciar nuevo juego")
        print("2. Salir")
        print(f"{'_':_^30}")

    def registrar_usuario(self):
        print("\nHola, bienvenid@ al juego de blackjack")
        nombre: str = input("¿Cuál es tu nombre?: ")
        self.blackjack.registrar_usuario(nombre)

    def ejecutar_app(self):
        self.registrar_usuario()
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def iniciar_nuevo_juego(self):
        apuesta: int = self.pedir_apuesta()
        self.blackjack.iniciar_juego(apuesta)
        self.mostrar_manos(self.blackjack.cupier.mano, self.blackjack.jugador.mano)

        if not self.blackjack.jugador.mano.es_blackjack():
            self.hacer_jugada_del_jugador()
        else:
            print(f"FELICITACIONES, LOGRASTE BLACKJACK. HAS GANADO EL JUEGO")

    def hacer_jugada_del_jugador(self):
        while not self.blackjack.jugador_perdio():
            respuesta = input("¿Quiere otra carta? s(si), n(no): ")
            if respuesta == "s":
                self.blackjack.repartir_carta_a_jugador()
                self.mostrar_manos(self.blackjack.cupier.mano, self.blackjack.jugador.mano)
            elif respuesta == "n":
                break

        if self.blackjack.jugador_perdio():
            print("\nHAS PERDIDO EL JUEGO")
        else:
            self.ejecutar_turno_de_la_casa()

    def ejecutar_turno_de_la_casa(self):
        self.blackjack.cupier.mano.destapar()
        
        self.mostrar_manos(self.blackjack.cupier.mano, self.blackjack.jugador.mano)
        
        while True:
            valor_cupier = self.blackjack.cupier.mano.calcular_valor()
            if isinstance(valor_cupier, str):
                print("\nNo se puede determinar el valor de la mano de la casa.")
                return
            if valor_cupier >= 17:
                break
            self.blackjack.repartir_carta_a_la_casa()
            self.mostrar_manos(self.blackjack.cupier.mano, self.blackjack.jugador.mano)
            
        valor_cupier = self.blackjack.cupier.mano.calcular_valor()
        valor_jugador = self.blackjack.jugador.mano.calcular_valor()
        
        if isinstance(valor_cupier, str):
            print("\nNo se puede determinar el valor de la mano de la casa.")
            return
        
        if valor_cupier > 21:
            print("\nFELICITACIONES, LA CASA SE PASÓ. HAS GANADO EL JUEGO")
        elif valor_cupier == 21 and len(self.blackjack.cupier.mano.cartas) == 2:
            print("\nHAS PERDIDO EL JUEGO, LA CASA TIENE BLACKJACK")
        else:
            if isinstance(valor_jugador, str):
                print("\nNo se puede determinar el valor de la mano del jugador.")
                return
            if valor_cupier > valor_jugador:
                print("\nHAS PERDIDO EL JUEGO")
            elif valor_cupier < valor_jugador:
                print("\nFELICITACIONES, HAS GANADO EL JUEGO")
            else:
                print("\nEMPATE")

    def pedir_apuesta(self):
        apuesta: int = int(input("¿Cuál es su apuesta?: "))
        while not self.blackjack.jugador.puede_apostar(apuesta) or apuesta <= 0:
            print(f"ADVERTENCIA: No tiene suficientes fichas para apostar {apuesta} o su apuesta fue de 0")
            print("Ingrese una nueva apuesta.")
            apuesta = int(input("¿Cuál es su apuesta?: "))
        return apuesta

    @staticmethod
    def mostrar_manos(mano_casa, mano_jugador):
        print(f"\n{'MANO DE LA CASA':<15}\n{str(mano_casa):<15}")
        print(f"{'VALOR: ' + str(mano_casa.calcular_valor()):<15}")
        print(f"\n{'TU MANO':<15}\n{str(mano_jugador):<15}")
        print(f"{'VALOR: ' + str(mano_jugador.calcular_valor()):<15}")

    @staticmethod
    def salir():
        print("\nGRACIAS POR JUGAR BLACKJACK. VUELVA PRONTO")
        sys.exit(0)



