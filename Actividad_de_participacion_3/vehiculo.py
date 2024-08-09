class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje=0):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

mi_carro = Vehiculo(120, 15000)

print(mi_carro.velocidad_maxima)

print("Mi carro tiene una velocidad máxima de: {} Km/h".format(mi_carro.velocidad_maxima))
print("Mi carro tiene un kilometraje de: {} Km".format(mi_carro.kilometraje))

