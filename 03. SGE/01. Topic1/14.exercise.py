# Ejemplo de: map
# La lista
lista = [1, 2, 3]

# La función
def cuadrado(n):
    return n*n

# La prueba
print("Lista resultante: " + str(list(map(cuadrado, lista))))