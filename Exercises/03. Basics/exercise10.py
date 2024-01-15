# Introducir una cadena de caracteres e indicar si es un palíndromo.

cad = input("Introduce una cadena:")
if cad.lower() == cad[::-1].lower():
	print("Es un palíndromo")
else:
	print("No es un palíndromo")
