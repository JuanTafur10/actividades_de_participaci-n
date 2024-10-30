from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, valor):
        pass

    def _validar_longitud(self, valor):
        return len(valor) >= self._longitud_esperada
    
    def _contiene_mayuscula(self, valor):
        return any(char.isupper() for char in valor)

    def _contiene_minuscula(self, valor):
        return any(char.islower() for char in valor)

    def _contiene_numero(self, valor):
        return any(char.isdigit() for char in valor)