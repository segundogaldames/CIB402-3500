print("Ingrese tres valores numericos iguales")

num1 = int(input("Ingrese el valor 1: "))
num2 = int(input("Ingrese el valor 2: "))
num3 = int(input("Ingrese el valor 3: "))

if num1 == num2 and num1 == num3:
    suma = num1 + num2
    producto = suma * num3
    print("La suma del los dos primeros valores es: ", suma)
    print("El producto de la suma por el tercer valor es: ", producto)
else:
    print("Uno de los tres valores ingresados no es igual")