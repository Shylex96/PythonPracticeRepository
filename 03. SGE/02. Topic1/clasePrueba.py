from clasePersona import Persona # Importar clase Persona

p1 = Persona('Ana', 45) # Crear persona p1
print(p1.getNombre()) # Mostrar su nombre
nombre = input("Dame el nombre de una persona")
p1.setNombre(nombre) # Asignar nuevo nombre
print(p1.getNombre()) # Mostrar su nombre
p1.mostrar_edad() # Se llama a un método de la clase
p1.modificar_edad(21) # Es posible cambiar la edad usando el método específico que hemos hecho para hacerlo de forma controlada
p1.mostrar_edad()