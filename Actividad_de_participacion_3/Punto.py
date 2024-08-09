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

    


punto_a = Punto("A", 3, 4)
punto_a.mostrar()  

punto_b = Punto("B", -2, 1)
punto_b.mostrar()  

punto_a.mover(2, 1)  
punto_a.mostrar() 

punto_b.mover(-1, 3) 
punto_b.mostrar()
    
