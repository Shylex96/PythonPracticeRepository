import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "informatica", "desarrollo", "openai", "inteligencia"]
    return random.choice(palabras).upper()

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    resultado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jugar():
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    intentos_maximos = 6
    intentos_actuales = 0

    print("¡Bienvenido al Juego de la Horca!")
    print(mostrar_tablero(palabra_secreta, letras_adivinadas))

    while intentos_actuales < intentos_maximos:
        letra = input("Ingresa una letra: ").upper()

        if letra in letras_adivinadas:
            print("Ya has intentado con esa letra. Intenta otra.")
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra_secreta:
            intentos_actuales += 1
            print(f"Incorrecto. Te quedan {intentos_maximos - intentos_actuales} intentos.")
        else:
            print("¡Correcto!")

        tablero = mostrar_tablero(palabra_secreta, letras_adivinadas)
        print(tablero)

        if "_" not in tablero:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

    if "_" in mostrar_tablero(palabra_secreta, letras_adivinadas):
        print(f"¡Oh no! Has perdido. La palabra era {palabra_secreta}.")

if __name__ == "__main__":
    jugar()
