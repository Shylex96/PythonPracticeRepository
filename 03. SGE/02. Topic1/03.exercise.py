# Lo primero, importar el módulo
import sys

# Versión API del motor de Python
versionAPI = sys.api_version
print("Versión API: " + str(versionAPI))

# Codificación de los caracteres por defecto
codificacion = sys.getdefaultencoding()
print("Codificación: " + str(codificacion))

# Mostrar contenido del PATH
pathActual = sys.path
print("PATH actual: " + str(pathActual))

# Mostrar plataforma sobre la que se ejecuta este programa
plataforma = sys.platform
print("Plataforma actual: " + str(plataforma))

# Versión del intérprete de Python
version = sys.version
print("Versión del intérprete: " + str(version))

# Mostrar tamaño en bytes de un objeto
tamano = sys.getsizeof("Hola")
print("Tamaño de \"Hola\": " + str(tamano))

# Mostrar un diccionario con los módulos cargados
print(sys.modules)
# Salir
sys.exit()