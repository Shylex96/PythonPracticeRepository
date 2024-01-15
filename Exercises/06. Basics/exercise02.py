# Escribe un programa que solicite al usuario una lista de números y un índice. 
# Luego, intenta acceder al valor en el índice proporcionado. 
# Asegúrate de manejar la excepción de índice fuera de rango.

# Ejercicio 2: Acceso a índice fuera de rango

try:
    numeros = [int(x) for x in input("Ingresa una lista de números separados por espacio: ").split()]
    indice = int(input("Ingresa un índice: "))

    valor = numeros[indice]

    print(f"Valor en el índice {indice}: {valor}")

except IndexError:
    print("Error: Índice fuera de rango.")
except ValueError:
    print("Error: Ingresa un índice válido.")
