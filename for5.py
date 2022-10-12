cantidad = 0
n = int(input("Ingrese la cantidad de numeros a evaluar: "))

for x in range(n):
    num = int(input("Ingrese el valor " + str(x+1) + ": "))

    if num >= 1000:
        cantidad += 1

print("El numero de valores mayor que mil es ", cantidad)