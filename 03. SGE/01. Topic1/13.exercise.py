# Función que no devuelve nada, o sea None
def funcion1():
    print("No devuelve nada")
# Uso de la función
print(funcion1())

# Función con parámetros optativos o por defecto
def funcion2(parametro1, parametro2="Hola", parametro3=(True, 2)):
    return("Parámetros: " + str(parametro1) + ", " + str(parametro2) + ", " +
str(parametro3))

# Uso de la función con todos los parámetros
print(funcion2(1,2,3))

# Uso de la función con un único parámetro, el obligatorio
print(funcion2(1))

# Uso de la función con un parámetro con su orden cambiado
print(funcion2("x", parametro3=23))

# Función con número indeterminado de parámetros
def funcion3(*parametros):
    suma = 0
    for elemento in parametros:
        suma = suma + elemento
    return suma

# Uso de la función con dos parámetros
print(funcion3(1,2))
# Uso de la función con cinco parámetros
print(funcion3(1,2,3,4,5))