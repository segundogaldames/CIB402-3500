num = int(input("Ingrese un numero mayor que cero: "))
contador = 1

if num > 0:
    while contador <= num:
        print(contador)
        contador += 1
else:
    print("El numero ingresado no es mayor que cero")