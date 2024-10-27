from item_compra import ItemCompra
from libro import Libro

class CarroCompras:
    def __init__(self):
        self.items = []

    def agregar_item(self, libro: Libro, cantidad: int) -> ItemCompra:
        item = ItemCompra(libro, cantidad)
        self.items.append(item)
        return item

    def calcular_total(self) -> float:
        total = sum(item.calcular_subtotal() for item in self.items)
        return total

    def quitar_item(self, isbn: str):
        self.items = [item for item in self.items if item.ibro.isbn != isbn]

