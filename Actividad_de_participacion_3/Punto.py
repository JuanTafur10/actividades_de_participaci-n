class Punto:
    def __init__(self, nombre,  x, y):
        self.nombre = nombre        
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Las Coordenadas del punto son {self.nombre}: ({self.x}, {self.y})")

punto_a = Punto("A", 3, 4)
punto_a.mostrar()  

punto_b = Punto("B", -2, 1)
punto_b.mostrar()  