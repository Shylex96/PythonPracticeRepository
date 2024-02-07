class Persona: # Nombre de la clase. También class Persona(object):
    def __init__(self, nombre, edad): #Constructor
        self.nombre = nombre # Un atributo cualquiera
        self.edad = edad # Otro atributo cualquiera

    def mostrar_edad(self): # Es necesario que, al menos, tenga el parámetro self
        print(self.edad) # Mostrando un atributo

    def modificar_edad(self, edad): # Modificando Edad
        if edad < 0 or edad > 150: # Se comprueban condiciones para la edad
            return False
        else: # Si está en el rango 0-150, entonces se modifica la variable
            self.edad = edad # Se modifica la edad

    def getNombre(self): # Inspectores
        return self.nombre

    def setNombre(self, n):
        self.nombre = n
