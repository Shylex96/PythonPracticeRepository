try:
    f = open("miFichero.txt","r") # Abrir fichero para leer
except Exception:
    exit()
fin = False # Variable para controlar fin del bucle
while not fin: # Bucle para recorrer fichero
    print("Posición del cursor: "+str(f.tell())) # Indicar posición del cursor
    linea = f.readline() # Lectura de una línea
    if not linea: # Comprobar si hemos llegado a fin de fichero
        fin = True
    else:
        print(linea) # Mostrar línea leída
f.close() # Cerrar
