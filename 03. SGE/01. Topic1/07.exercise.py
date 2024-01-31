# listas -> []
# tuplas -> ()

# coding: utf-8
'''
Created on 4 ene. 2018
@author: Studium
'''
lista = ["abc", 42, 3.1415]
print(lista[0]) # Acceder a un elemento por su índice
print(lista[-1]) # Acceder a un elemento usando un índice negativo
lista.append(True) # Añadir un elemento al final de la lista
print(lista) #Equivalente a for i in lista: print(i)
del lista[3] # Borra un elemento de la lista usando un índice (en este caso: True)
lista[0] = "xyz" # Re-asignar el valor del primer elemento de la lista
print(lista[0:2]) # Mostrar los elementos de la lista del índice "0" al "2" (sin incluir este último)
lista_anidada = [lista, [True, 42]] # Es posible anidar listas
print(lista_anidada)
print(lista_anidada[1][0]) # Acceder a un elemento de una lista dentro de otra lista (del segundo elemento, mostrar el primer elemento)