#Ejemplo de: filter

# La lista
lista = [1, 2, 3, 4, 5, 6, 7, 8]

# La función
def par(n):
    return (n%2==0)

# La prueba
print("Lista resultante: " + str(list(filter(par, lista))))