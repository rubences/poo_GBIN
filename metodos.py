colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }

def GET(clave, valor_defecto):
    return colores.get(clave, valor_defecto)

def KEYS():
    return list(colores.keys())

print(GET("amarillo", "no existe"))
print(KEYS()) 
