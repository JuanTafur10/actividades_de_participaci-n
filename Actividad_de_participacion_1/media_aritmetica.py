def media_aritmetica(numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    media = suma / cantidad
    
    return media

entrada = input("Ingrese una lista de números separados por comas: ")
numeros = [float(num) for num in entrada.split(",")]


resultado = media_aritmetica(numeros)

print(f"La media aritmética de la lista es: {resultado}")