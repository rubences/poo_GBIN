from copy import copy

class Test:
    pass

test1 = Test()
test2 = copy(test1)

test1.algo = "Prueba"

print(test2 == test1)  # ¿Son el mismo objeto?

try:
    print(test2.algo)
except Exception as e:
    print(e)

