class Alumno:
    def __init__(self, nombre, apellidos, edad, asignaturas, notas):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.asignaturas = asignaturas
        self.notas = notas

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print("Asignaturas y Notas:")
        for i in range(len(self.asignaturas)):
            print(f"  {self.asignaturas[i]}: {self.notas[i]}")
        print("\n")