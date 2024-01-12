# Solicitar al usuario las notas obtenidas en los diferentes componentes
parcial1 = float(input("Escribe la nota obtenida en el primer parcial: "))
parcial2 = float(input("Escribe la nota obtenida en el segundo parcial: "))
parcial3 = float(input("Escribe la nota obtenida en el tercer parcial: "))
examen = float(input("Escribe la nota obtenida en tu examen final: "))
trabajo = float(input("Escribe la nota obtenida en el trabajo final: "))

# Calcular la nota final según el peso de cada componente
nota = ((parcial1 + parcial2 + parcial3) / 3) * 0.55 + (0.3 * examen) + (0.15 * trabajo)

# Mostrar la nota final al usuario
print("La nota es:", nota)
print("La nota redondeada 1º forma es: %.2f" %nota)
print("La nota redondeada 2º forma es: {:.2f}".format(nota))
nota_redondeada = round(nota, 2)
print("La nota redondeada 3º forma es:", nota_redondeada)