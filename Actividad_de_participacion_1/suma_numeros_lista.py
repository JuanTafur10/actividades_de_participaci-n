def suma_numeros_lista(numeros):
    return sum(numeros)

Lista = input("Ingrese una lista de números separados por comas: ")

numeros = [float(numero) for numero in Lista.split(",")]

suma = suma_numeros_lista(numeros)

print(f"La suma de los números en la lista es: {suma}")