def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)



numero = int(input("Ingrese un número para calcular su factorial: "))

resultado = factorial(numero)

print(f"El factorial de {numero} es {resultado}")