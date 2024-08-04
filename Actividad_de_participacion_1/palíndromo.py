cadena = input("Ingrese una cadena de texto: ")

cadena_limpia = cadena.replace(" ", "").lower()

palindromo = cadena_limpia == cadena_limpia[::-1]


if palindromo:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")