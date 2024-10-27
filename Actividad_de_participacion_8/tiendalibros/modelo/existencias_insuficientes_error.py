from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    
    def __init__(self, titulo: str, isbn: str, cantidad_a_comprar: int):
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar
        super().__init__()

    def __str__(self):
        return (f"El libro con titulo {self.titulo} y isbn {self.isbn} no tiene suficientes existencias "
                f"para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}")
