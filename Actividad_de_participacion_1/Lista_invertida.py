def invertir_lista(lista):
    return lista[::-1]

entrada = input("Ingrese una lista de elementos separados por comas: ")

lista = entrada.split(",")

lista_invertida = invertir_lista(lista)


print(f"Lista original: {lista}")
print(f"Lista invertida: {lista_invertida}")