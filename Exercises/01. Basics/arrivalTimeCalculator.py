# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.

# Solicitar al usuario la hora de partida y el tiempo de viaje en segundos
hora_salida = int(input("Hora de salida: "))
minutos_salida = int(input("Minutos de salida: "))
segundos_salida = int(input("Segundos de salida: "))
tiempo_viaje = int(input("Tiempo que has tardado en segundos: "))

# Convertir la hora de salida a segundos
seg_inicial = hora_salida * 3600 + minutos_salida * 60 + segundos_salida

# Sumar los segundos que ha tardado
seg_final = seg_inicial + tiempo_viaje

# Convertir los segundos totales a hora, minuto y segundos
hora_llegada = seg_final // 3600
minutos_llegada = (seg_final % 3600) // 60
segundos_llegada = (seg_final % 3600) % 60

# Mostrar la hora de llegada
print("Hora de llegada")
print(hora_llegada, ":", minutos_llegada, ":", segundos_llegada)
