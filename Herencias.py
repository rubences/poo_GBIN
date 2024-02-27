class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este método lo heredo de A")

class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este método lo heredo de B")

class C(B,A):
    def c(self):
        print("Este método es de C")

print("Clase A")
clase_a = A()
clase_a.a()
print("Clase B")
clase_b = B()
clase_b.b()
print("Clase C")
clase_c = C()
clase_c.a()
clase_c.b()
clase_c.c()

