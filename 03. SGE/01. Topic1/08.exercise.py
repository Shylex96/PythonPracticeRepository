# Leer de teclado palabras y guardarlas en una lista hasta que se escriba un punto 

pedirPalabras = ""
listaPalabras = []
comando = "."


while pedirPalabras != comando:
    pedirPalabras = (str(input("Escribe una palabra: \n")))

    if (pedirPalabras != comando):
        listaPalabras.append(pedirPalabras)
    
print(listaPalabras)