# Lo primero, importar el módulo
import os

# Ejecutar comandos del Sistema Operativo
# Mostrar el nombre del sistema operativo
sistemaOperativo = os.name
print("Sistema Operativo: " + str(sistemaOperativo))

# Mostrar directorio actual
directorioActual = os.getcwd()
print("Directorio actual: " + str(directorioActual))

# Diferentes funciones del directorio actual
print("Path absoluto: " + str(os.path.abspath(directorioActual)))
print("Path base: " + str(os.path.basename(directorioActual)))
print("Nombre del directorio del fichero: " + str(os.path.dirname("C:\\Users\\StudiumFormacion LOL\\Desktop\Esteban\\VSC Python GitHub\\03. SGE\\02. Topic1\\01.exercise.py")))
print("¿Es directorio?: " + str(os.path.isdir(directorioActual)))
print("¿Es fichero?: " + str(os.path.isfile(directorioActual)))
print("La unidad es: " + str(os.path.splitdrive(directorioActual)[0]))

# Mostrar PID del proceso activo, este programa
pidProceso = os.getpid()
print("PID: " + str(pidProceso))

# Mostrar Ruta de ejecución
ruta = os.defpath
print("Ruta: " + str(ruta))

# Mostrar contenido del PATH
path = os.environ
print("PATH: " + str(path))

# Mostrar contenido del directorio en forma de lista pasado como parámetro
contenido = os.listdir("C:")
print("Contenido: " + str(contenido))

# Tratamiento de los elementos de un directorio
for fichero in os.listdir("C:"):
    print("Nombre fichero/directorio: "+fichero)

'''
# Ahora, para cada directorio de forma recursiva, mostrar el contenido
for path, dirs, ficheros in os.walk("C:"):
    for fichero in ficheros: # Recorremos los ficheros encontrados
        nombreFichero = os.path.join(path, fichero)
    print("Tamaño de " + str(nombreFichero) + " es " +str(os.path.getsize(nombreFichero))+ " bytes")
# Crea un directorio en la ruta especificada
os.mkdir("C:\\ejemplo")
'''