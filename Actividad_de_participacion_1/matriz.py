import random

def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = [random.randint(0, 100) for _ in range(columnas)]
        matriz.append(fila)
    return matriz


def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))


filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))


matriz = generar_matriz(filas, columnas)


print("Matriz generada:")
imprimir_matriz(matriz)