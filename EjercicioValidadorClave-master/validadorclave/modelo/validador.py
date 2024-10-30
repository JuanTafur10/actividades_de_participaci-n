from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    @abstractmethod
    def es_valida(self, valor):