palabra1 = str(input("Dime una palabra:\n"))
palabra2 = str(input("Dime otra palabra:\n"))

if (palabra1.lower() == palabra2.lower()):
    print("Las palabras son iguales")
else:
    print("La suma de las longitudes es:", len(palabra1)+len(palabra2))
    print(f"La suma de las longitudes es: {len(palabra1)+len(palabra2)}")
    
    '''
    lenPalabra1 = len(palabra1)
    lenPalabra2 = len(palabra2)
    print(lenPalabra1+lenPalabra2)
    '''