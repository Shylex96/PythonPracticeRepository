# Crear dos listas, una con palabras en español y otra con palabras en inglés para crear un diccionario. 
# Leer de teclado una palabra en español (de las existentes) y mostrar su traducción.

tuplaEsp = ("Hola", "Adiós", "Ayuda", "Coche")
tuplaEng = ("Hello", "Goodbye", "Help", "Car")

print("Por favor, escribe una palabra en español del listado: ")
print(tuplaEsp)

palabraBusqueda = (str(input("Palabra: \n")))

acceso = tuplaEsp.index(palabraBusqueda)
print(tuplaEng[acceso])

