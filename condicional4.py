num1 = int(input("Ingrese el valor 1: "))
num2 = int(input("ingrese el valor 2: "))
num3 = int(input("Ingrese el valor 3: "))

if num1 > num2 and num1 > num3:
    print("el primer valor ingresado es mayor: ", num1)
else:
    if num2 > num3:
        print("El segundo valor ingresado es mayor: ", num2)
    else:
        print("El tercer valor es mayor: ", num3)