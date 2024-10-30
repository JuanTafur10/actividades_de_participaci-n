from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, valor):
        pass

    def _validar_longitud(self, valor):
        return len(valor) >= self._longitud_esperada