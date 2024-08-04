def numero_mayor_menor(numeros):
    numero_mayor = max(numeros)
    numero_menor = min(numeros)
    return numero_mayor, numero_menor

entrada = input("Ingrese una lista de números separados por comas: ")

numeros = [float(numero) for numero in entrada.split(",")]

mayor, menor = numero_mayor_menor(numeros)


print(f"El número más grande en la lista es: {mayor}")
print(f"El número más pequeño en la lista es: {menor}")