pedirNumero = 0
lista = []

while pedirNumero != 9:
    pedirNumero += 1
    num = int(input("Escribe un número: \n"))
    
    lista.append(num)
print("\nMatriz de 3x3:\n\n",lista[0],lista[1],lista[2],"\n",lista[3],lista[4],lista[5],"\n",lista[6],lista[7],lista[8])