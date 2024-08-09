class Rectangulo:
    def __init__(self, nombre, esquina1, esquina2):
        self.nombre = nombre
        self.esquina1 = esquina1
        self.esquina2 = esquina2
        
    def obtener_esquinas(self):
        esquina3 = (self.esquina1[0], self.esquina2[1])
        esquina4 = (self.esquina2[0], self.esquina1[1])
        return {
            "Esquina_1": self.esquina1,
            "Esquina_2": self.esquina2,
            "Esquina_3": esquina3,
            "Esquina_4": esquina4
        }
    
    def calcular_ancho(self):
        return abs(self.esquina2[0] - self.esquina1[0])

    def calcular_alto(self):
        return abs(self.esquina2[1] - self.esquina1[1])

    def calcular_perimetro(self):
        ancho = self.calcular_ancho()
        alto = self.calcular_alto()
        return 2 * (ancho + alto)
    
    def calcular_area(self):
        ancho = self.calcular_ancho()
        alto = self.calcular_alto()
        return ancho * alto
    
    def es_cuadrado(self):
        return self.calcular_ancho() == self.calcular_alto()
    
    
Rectangulo_A = Rectangulo("Rectangulo_A", (1, 2), (4, 5))

esquinas = Rectangulo_A.obtener_esquinas()
for nombre, ubicacion in esquinas.items():
    print(f"{Rectangulo_A.nombre} = {nombre}: {ubicacion}")

perimetro = Rectangulo_A.calcular_perimetro()
print(f"Perímetro de {Rectangulo_A.nombre}: {perimetro}")

area = Rectangulo_A.calcular_area()
print(f"Área de {Rectangulo_A.nombre}: {area}")

if Rectangulo_A.es_cuadrado():
    print(f"{Rectangulo_A.nombre} es un cuadrado")
else:
    print(f"{Rectangulo_A.nombre} no es un cuadrado")