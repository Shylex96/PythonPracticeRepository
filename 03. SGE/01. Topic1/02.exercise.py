cadena1="cadena de pruebas"
cadena2="otra cadena de pruebas"
cadena3="Cadena con {} parámetros {}"
print(cadena1, cadena2) # Concatenar dejando espacio entre ambas
print(cadena1+cadena2) # Concatenar sin dejar espacio entre ambas
print(cadena1+ " "+ cadena2) # Concatenar
print(cadena1.capitalize())
print(cadena1.center(50,'*'))
print(cadena1.ljust(50,'*'))
print(cadena1.rjust(50,'*'))
print("La letra a aparece " + str(cadena1.count("a")) + " veces")
print(cadena1.find("a"))
print(cadena1.find("x"))
print(cadena1.upper())
print(cadena1.lower())
print(cadena1.strip('c'))
print(cadena1.split())
print(len(cadena1))
print(cadena1.join(cadena2))
print(cadena3.format(2,"tipo corchete"))