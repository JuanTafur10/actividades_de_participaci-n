class Carta:
    CORAZONES = "Corazones"
    DIAMANTES = "Diamantes"
    TREBOLES = "Treboles"
    PICAS = "Picas"

    def __init__(self, valor, pinta):
        if pinta in [self.CORAZONES, self.DIAMANTES, self.TREBOLES, self.PICAS]:
            self.valor = valor
            self.pinta = pinta
        else:
            self.valor = None
            self.pinta = None

    def __str__(self):
        if self.valor is not None and self.pinta is not None:
            return f"La carta es {self.valor} de {self.pinta}"
        else:
            return "No es una carta válida"
    
carta1 = Carta("As", Carta.PICAS)
print(carta1)  

