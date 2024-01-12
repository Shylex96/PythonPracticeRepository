a = int(input("Introduce el valor de la variable A: "))
b = int(input("Introduce el valor de la variable B: "))

print("\nEl valor de la variable A es: ", a)
print("El valor de la variable B es: ", b)

aux = a
a = b
b = aux

print("\nEl valor de la variable A tras conversión es: ", a)
print("El valor de la variable B tras conversión es: ", b)