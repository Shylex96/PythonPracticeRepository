try:
    f = open("miFichero.txt","a") # Abrir fichero para añadir
except Exception:
    exit()

f.write("Mensaje inicial\n") # Añadir texto
f.close() # Cerrar
print("Guardando datos…")