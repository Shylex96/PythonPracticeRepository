# Crear dos listas, una con palabras en español y otra con palabras en inglés para crear un diccionario. 
# Leer de teclado una palabra en español (de las existentes) y mostrar su traducción.
# Comprobar si la palabra existe. En caso de que no devolver un mensaje y volver a preguntar por otra.

tuplaEsp = ("Hola", "Adiós", "Ayuda", "Coche")
tuplaEng = ("Hello", "Goodbye", "Help", "Car")

print("Por favor, escribe una palabra en español del listado: ")
print(tuplaEsp)


def diccionario():
    
    palabraBusqueda = (str(input("Palabra: \n")))
   
    if(palabraBusqueda in tuplaEsp):
        acceso = tuplaEsp.index(palabraBusqueda)
        print(tuplaEng[acceso])
    else:
        print("Palabra no encontrada")
        # diccionario()


diccionario()
