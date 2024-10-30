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
    
class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self, longitud_esperada):
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self, valor):
        caracteres_especiales = "@_#$%"
        return any(char in caracteres_especiales for char in valor)