class Circulo:
    def __init__(self, nombre = "Circulo_A"):
        self.nombre = nombre
        self.centro = 0,0
        self.radio = 5

    def calcular_perimetro(self):
        return 2 * 3.1416 * self.radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)
    
    def pertenece_al_circulo(self, punto):
        distancia_al_centro = ((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2) ** 0.5
        return distancia_al_centro <= self.radio

circulo = Circulo()

print(f"El centro del {circulo.nombre} es:")
print(f"  X: {circulo.centro[0]:.2f}")
print(f"  Y: {circulo.centro[1]:.2f}")
print(f"El radio del {circulo.nombre} es: {circulo.radio:.2f}")

perimetro = circulo.calcular_perimetro()
print(f"El perímetro del {circulo.nombre} es: {perimetro:.2f}")

area = circulo.calcular_area()
print(f"El área del {circulo.nombre} es: {area:.2f}")

punto = (3, 4)
if circulo.pertenece_al_circulo(punto):
    print(f"El punto ({punto[0]}, {punto[1]}) pertenece al {circulo.nombre}")
else:
    print(f"El punto ({punto[0]}, {punto[1]}) no pertenece al {circulo.nombre}")