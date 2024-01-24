def contador():
    num = int(input("Dame un número: "))
    suma = 0
    while num != 0:
       suma = suma + num
       num = int(input("Dame otro número: "))
    print("La suma total es:",suma)   

contador()