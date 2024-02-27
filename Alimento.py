from Producto import Producto

class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __init__(self, referencia, nombre, pvp, descripcion, productor, distribuidor):
        super().__init__(referencia, nombre, pvp, descripcion)
        self.productor = productor
        self.distribuidor = distribuidor

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"PRODUCTOR\t\t {self.productor}\n" \
               f"DISTRIBUIDOR\t\t {self.distribuidor}\n"


manzana = Alimento(2035, "Manzana", 5, "Manzana roja", "Gallardo", "La Chiquita")
print(manzana)