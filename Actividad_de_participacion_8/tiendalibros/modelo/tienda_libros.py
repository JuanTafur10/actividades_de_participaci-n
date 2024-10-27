from libro import Libro
from carro_compra import CarroCompras
from libro_error import LibroError

class LibroExistenteError(LibroError):
    def __init__(self, libro):
        super().__init__()
        self.libro = libro

    def __str__(self):
        return f"El libro con titulo {self.libro.titulo} y isbn: {self.libro.isbn} ya existe en el catálogo"

class LibroAgotadoError(LibroError):
    def __init__(self, libro):
        super().__init__()
        self.libro = libro

    def __str__(self):
        return f"El libro con titulo {self.libro.titulo} y isbn {self.libro.isbn} esta agotado"

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, libro, cantidad_a_comprar):
        super().__init__()
        self.libro = libro
        self.cantidad_a_comprar = cantidad_a_comprar

    def __str__(self):
        return f"El libro con titulo {self.libro.titulo} y isbn {self.libro.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.libro.existencias}"

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError(self.catalogo[isbn])
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro

    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro)
        if libro.existencias < cantidad:
            raise ExistenciasInsuficientesError(libro, cantidad)
        self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)

    