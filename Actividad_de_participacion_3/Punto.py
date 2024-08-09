class Punto:
    def __init__(self, nombre,  x, y):
        self.nombre = nombre        
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Las Coordenadas del punto {self.nombre} son: ({self.x}, {self.y})")

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"El punto {self.nombre} se ha movido {dx} unidades en X y {dy} unidades en Y")

    def calcular_distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        distancia = (dx**2 + dy**2)**0.5
        return print(f"La distancia entre el punto {self.nombre} y el punto {otro_punto.nombre} es: {distancia:.2f}")
        
    


punto_a = Punto("A", 3, 4)

punto_a.mostrar()  

punto_a.mover(2, 1)  

punto_a.mostrar() 

punto_c = Punto("C", 5, 0)
punto_a.calcular_distancia(punto_c)
