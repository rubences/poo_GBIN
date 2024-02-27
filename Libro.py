from Producto import Producto

class Libro(Producto):
    isbn = ""
    autor = ""

    def __init__(self, referencia, nombre, pvp, descripcion, isbn, autor):
        super().__init__(referencia, nombre, pvp, descripcion)
        self.isbn = isbn
        self.autor = autor

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"ISBN\t\t {self.isbn}\n" \
               f"AUTOR\t\t {self.autor}\n"
