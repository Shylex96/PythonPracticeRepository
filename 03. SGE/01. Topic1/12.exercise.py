# Crear dos listas, una con palabras en español y otra con palabras en inglés para crear un diccionario. 
# Leer de teclado una palabra en español (de las existentes) y mostrar su traducción.
# Comprobar si la palabra existe de forma alternativa al ejercicio 10. 
# Usar diccionarios 

diccionarioPalabras =  {"Hola": "Hello", "Adiós": "GoodBye", "Ayuda": "Help", "Coche": "Car"}

print("Por favor, escribe una palabra en español del listado: ")


def diccionario():
    
    palabraBusqueda = (str(input("Palabra: \n")))
   
    try:
        print(diccionarioPalabras[palabraBusqueda])
    except Exception:
        print("Palabra no encontrada.")


diccionario()
