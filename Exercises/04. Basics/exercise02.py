# Crea una lista e inicalizala con 5 cadenas de caracteres leídas por teclado. 
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra 
# sus elementos  por la pantalla.

lista1 = []
lista2 = []
# Recorremos la lista1 y leemos cada elemento por teclado.
for indice in range(1,6):
	lista1.append(input("Dame la cadena %d:" % indice))
	
# Copiamos la lista1 en la lista2 en orden inverso
lista2 = lista1[::-1]

# Recorremos el vector2 para mostrarlo
for cadena in lista2:
	print(cadena)
