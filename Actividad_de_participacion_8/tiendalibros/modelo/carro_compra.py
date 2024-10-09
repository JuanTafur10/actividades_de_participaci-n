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


libro1 = Libro(titulo="El Quijote", autor="Miguel de Cervantes", precio=20.0, isbn="1234567890")
libro2 = Libro(titulo="1984", autor="George Orwell", precio=15.0, isbn="0987654321")

carro = CarroCompras()
carro.agregar_item(libro1, 3)
carro.agregar_item(libro2, 2)

print(carro.calcular_total())  # Output: 90.0

carro.quitar_item("1234567890")
print(carro.calcular_total())  # Output: 30.0