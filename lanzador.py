from Adorno import Adorno
from Alimento import Alimento
from Libro import Libro
   

class ProductManager:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto, "\n")

    def mostrar_atributos_compartidos(self):
        for producto in self.productos:
            print(producto.referencia, producto.nombre)

    def mostrar_atributos_especificos(self):
        for producto in self.productos:
            if isinstance(producto, Adorno):
                print(producto.referencia, producto.nombre)
            elif isinstance(producto, Alimento):
                print(producto.referencia, producto.nombre, producto.productor)
            elif isinstance(producto, Libro):
                print(producto.referencia, producto.nombre, producto.isbn)

def agregar_producto(self, producto):
    self.productos.append(producto)


