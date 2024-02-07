# Ejemplo de: reduce³

from functools import reduce
# La lista
lista = [1, 2, 3, 4, 5, 6, 7, 8]

# La función
def suma(n,m):
    return(n+m)

# La prueba
print("Lista resultante: " + str(reduce(suma, lista)))