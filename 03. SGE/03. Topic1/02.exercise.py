try:
    f = open("miFichero.txt","w") # Abrir fichero para añadir machancando
except Exception:
    exit()
    
f.write("Mensaje nuevo\n") # Añadir texto
f.close() # Cerrar
print("Sobresescribiendo datos…")
