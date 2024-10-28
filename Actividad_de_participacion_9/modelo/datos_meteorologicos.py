class DatosMeteorologicos(): 
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]: 
        suma_temperatura = 0
        count_temperaturas = 0
        suma_humedad = 0
        count_humedad = 0
        suma_presion = 0
        count_presion = 0
        suma_viento = 0
        count_viento = 0
        suma_direccion_viento = 0
        count_direccion_viento = 0
        direcciones_a_grados = {
            "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5, "E": 90, "ESE": 112.5,
            "SE": 135, "SSE": 157.5, "S": 180, "SSW": 202.5, "SW": 225,
            "WSW": 247.5, "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
        }
        grados_a_direcciones = {v: k for k, v in direcciones_a_grados.items()}
        
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
                elif "Presión" in linea:
                    count_presion += 1
                    valor_presion = float(linea.split(":")[1].strip())
                    suma_presion += valor_presion
                    print(valor_presion)
                elif "Viento" in linea:
                    count_viento += 1
                    valor_viento = float(linea.split(":")[1].strip())
                    suma_viento += valor_viento
                    print(valor_viento)
                elif "Dirección" in linea:
                    count_direccion_viento += 1
                    direccion = linea.split(":")[1].strip()
                    grados = direcciones_a_grados[direccion]
                    suma_direccion_viento += grados
                    print(f"Dirección: {direccion}, Grados: {grados}")

        promedio_direccion_viento = suma_direccion_viento / count_direccion_viento if count_direccion_viento > 0 else 0
        direccion_predominante = min(direcciones_a_grados.keys(), key=lambda k: abs(direcciones_a_grados[k] - promedio_direccion_viento))
                

        print("suma_temperatura: ", suma_temperatura)
        print("count_temperaturas: ", count_temperaturas)
        print("promedio_temperaturas: ", suma_temperatura / count_temperaturas)

        print("suma_humedad: ", suma_humedad)
        print("count_humedad: ", count_humedad)
        print("promedio_humedad: ", suma_humedad / count_humedad)

        print("suma_presion: ", suma_presion)
        print("count_presion: ", count_presion)
        print("promedio_presion: ", suma_presion / count_presion)

        print("suma_viento: ", suma_viento)
        print("count_viento: ", count_viento)
        print("promedio_viento: ", suma_viento / count_viento)

        print("suma_direccion_viento: ", suma_direccion_viento)
        print("count_direccion_viento: ", count_direccion_viento)
        print("promedio_direccion_viento: ", promedio_direccion_viento)
        print("direccion_predominante: ", direccion_predominante)

