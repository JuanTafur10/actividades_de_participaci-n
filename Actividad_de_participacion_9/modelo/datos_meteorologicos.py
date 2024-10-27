class DatosMeteorologicos(): 
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]: 
        suma_temperatura = 0
        count_temperaturas = 0
        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo:
                if "Temperatura" in linea:
                    count_temperaturas += 1
                    valor = float(linea.split(":")[1].strip())
                    suma_temperatura += valor
                    print(valor)

        print("suma_temperatura: ", suma_temperatura)
        print("count_temperaturas: ", count_temperaturas)
