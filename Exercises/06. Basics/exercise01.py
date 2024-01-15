# Escribe un programa en Python que solicite al usuario dos números y realice la división
# del primero entre el segundo. Asegúrate de manejar la excepción de división entre cero.


# Ejercicio 1: División entre cero

try:
    numerador = float(input("Ingresa el numerador: "))
    denominador = float(input("Ingresa el denominador: "))

    resultado = numerador / denominador

    print(f"Resultado de la división: {resultado}")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Ingresa números válidos.")
