# Escribe un programa en Python que solicite al usuario ingresar tres notas: 
# una para el examen parcial, otra para el examen final y la última para los 
# trabajos prácticos. El programa debe calcular la calificación final del 
# estudiante utilizando las siguientes ponderaciones:
# El examen parcial tiene un peso del 30%.
#El examen final tiene un peso del 50%.
# Los trabajos prácticos tienen un peso del 20%.
# Finalmente, el programa debe mostrar la calificación final del estudiante.

# Solicitar al usuario ingresar las notas
nota_parcial = float(input("Ingrese la nota del examen parcial: "))
nota_final = float(input("Ingrese la nota del examen final: "))
nota_trabajos = float(input("Ingrese la nota de los trabajos prácticos: "))

# Calcular la calificación final con las ponderaciones
calificacion_final = (nota_parcial * 0.3) + (nota_final * 0.5) + (nota_trabajos * 0.2)

# Mostrar la calificación final al usuario
print("Calificación Final:", calificacion_final)
