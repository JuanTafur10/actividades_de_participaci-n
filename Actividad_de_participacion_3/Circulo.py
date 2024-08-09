class Circulo:
    def __init__(self, nombre, centro, radio):
        self.nombre = nombre
        self.centro = centro
        self.radio = radio

    def calcular_perimetro(self):
        return 2 * 3.1416 * self.radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)
    
    def pertenece_al_circulo(self, punto):
        distancia_al_centro = ((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2) ** 0.5
        return distancia_al_centro <= self.radio

Circulo_A = Circulo("Circulo_A", (0, 0), 5)


print(f"El centro del {Circulo_A.nombre} es:")
print(f"  X: {Circulo_A.centro[0]:.2f}")
print(f"  Y: {Circulo_A.centro[1]:.2f}")
print(f"El radio del {Circulo_A.nombre} es: {Circulo_A.radio:.2f}")

perimetro = Circulo_A.calcular_perimetro()
print(f"El perímetro del {Circulo_A.nombre} es: {perimetro:.2f}")

area = Circulo_A.calcular_area()
print(f"El área del {Circulo_A.nombre} es: {area:.2f}")


punto = (98, 85)
if Circulo_A.pertenece_al_circulo(punto):
    print(f"El punto ({punto[0]}, {punto[1]}) pertenece al {Circulo_A.nombre}")
else:
    print(f"El punto ({punto[0]}, {punto[1]}) no pertenece al {Circulo_A.nombre}")

