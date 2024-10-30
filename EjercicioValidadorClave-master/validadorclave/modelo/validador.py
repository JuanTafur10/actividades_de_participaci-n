from abc import ABC, abstractmethod
from errores import (
    NoCumpleLongitudMinimaError,
    NoTieneLetraMayusculaError,
    NoTieneLetraMinusculaError,
    NoTieneNumeroError,
    NoTieneCaracterEspecialError,
    NoTienePalabraSecretaError
)

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, valor):
        pass

    def _validar_longitud(self, valor):
        if len(valor) < self._longitud_esperada:
            raise NoCumpleLongitudMinimaError("La longitud mínima no se cumple")
        return True
    
    def _contiene_mayuscula(self, valor):
        if not any(char.isupper() for char in valor):
            raise NoTieneLetraMayusculaError("No contiene letra mayúscula")
        return True

    def _contiene_minuscula(self, valor):
        if not any(char.islower() for char in valor):
            raise NoTieneLetraMinusculaError("No contiene letra minúscula")
        return True

    def _contiene_numero(self, valor):
        if not any(char.isdigit() for char in valor):
            raise NoTieneNumeroError("No contiene número")
        return True
    
class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self, longitud_esperada):
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self, valor):
        caracteres_especiales = "@_#$%"
        if not any(char in caracteres_especiales for char in valor):
            raise NoTieneCaracterEspecialError("No contiene carácter especial")
        return True

    def es_valida(self, valor):
        return (self._validar_longitud(valor) and
                self._contiene_mayuscula(valor) and
                self._contiene_minuscula(valor) and
                self._contiene_numero(valor) and
                self.contiene_caracter_especial(valor))
    
class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self, longitud_esperada):
        super().__init__(longitud_esperada)

    def contiene_calisto(self, valor):
        palabra = "calisto"
        index = valor.lower().find(palabra)
        if index == -1:
            raise NoTienePalabraSecretaError("No contiene la palabra secreta 'calisto'")
        subcadena = valor[index:index+len(palabra)]
        mayusculas = sum(1 for char in subcadena if char.isupper())
        if not (2 <= mayusculas < len(palabra)):
            raise NoTienePalabraSecretaError("La palabra 'calisto' no cumple con las reglas de mayúsculas")
        return True

    def es_valida(self, valor):
        return (self._validar_longitud(valor) and
                self._contiene_mayuscula(valor) and
                self._contiene_minuscula(valor) and
                self._contiene_numero(valor) and
                self.contiene_calisto(valor))

class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, valor):
        return self.regla.es_valida(valor)