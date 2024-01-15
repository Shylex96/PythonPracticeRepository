# Escribe un programa que solicite al usuario el nombre de un archivo 
# y luego intente abrir y leer el contenido del archivo. 
# Asegúrate de manejar la excepción de archivo no encontrado.

# Ejercicio 3: Archivo no encontrado

try:
    nombre_archivo = input("Ingresa el nombre del archivo: ")

    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(f"Contenido del archivo:\n{contenido}")

except FileNotFoundError:
    print(f"Error: No se encuentra el archivo '{nombre_archivo}'.")
except IOError:
    print("Error: Ocurrió un problema al intentar leer el archivo.")
