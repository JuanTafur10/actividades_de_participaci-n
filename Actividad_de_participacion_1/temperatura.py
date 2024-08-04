
def f_to_c(temp):
  if temp < -459.67:
    return 'Temperatura no válida. El valor debe ser mayor o igual a -459.67 °F'
  else:
    return round((temp - 32) * 5 / 9, )

temp = float(input('Ingrese la temperatura en grados Fahrenheit: '))
celsius = f_to_c(temp)
print(f'{temp} °F son {celsius} °C')