# Funciones lambda

suma = lambda x, y = 2: x + y
print(suma(4)) # La variable "y" no se modifica, siendo su valor: 2
print(suma(4, 10)) # La variable "y" sí se modifica, siendo su nuevo valor: 10