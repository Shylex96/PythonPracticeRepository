from alumno import Alumno

def leer_archivo(archivo_alumnos= "registros.txt"):
    print("Hemos entrado en la función")
    alumnos = []
    with open(archivo_alumnos, "r") as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            nombre = lines[i].split(": ")[1].strip()
            apellidos = lines[i+1].split(": ")[1].strip()
            edad = int(lines[i+2].split(": ")[1])
            asignaturas = lines[i+3].split(": ")[1].strip().split(", ")
            notas = [float(x) for x in lines[i+4].split(": ")[1].strip().split(", ")]

            alumno = Alumno(nombre, apellidos, edad, asignaturas, notas)
            alumnos.append(alumno)

            i += 5
    return alumnos
    
def mostrar_alumnos(alumnos):
    for alumno in alumnos:
        alumno.mostrar()


archivo_alumnos = "registros.txt"
lista_alumnos = leer_archivo(archivo_alumnos)
Main.mostrar_alumnos(lista_alumnos)