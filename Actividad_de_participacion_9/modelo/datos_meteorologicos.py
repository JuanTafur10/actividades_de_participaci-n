class DatosMeteorologicos(): 
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]: 
        suma_temperatura = 0
        count_temperaturas = 0
        suma_humedad = 0
        count_humedad = 0
        
        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo:
                if "Temperatura" in linea:
                    count_temperaturas += 1
                    valor = float(linea.split(":")[1].strip())
                    suma_temperatura += valor
                    print(valor)
                elif "Humedad" in linea:
                        count_humedad += 1
                        valor_humedad = float(linea.split(":")[1].strip())
                        suma_humedad += valor_humedad
                        print(valor_humedad)

        print("suma_temperatura: ", suma_temperatura)
        print("count_temperaturas: ", count_temperaturas)
        print("promedio_temperaturas: ", suma_temperatura / count_temperaturas)

        print("suma_humedad: ", suma_humedad)
        print("count_humedad: ", count_humedad)
        print("promedio_humedad: ", suma_humedad / count_humedad)
