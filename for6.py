contador = 0
suma = 0
cont = 0
print("Ingrese 10 valores: ")

for x in range(1,11):
    num = int(input("Ingrese el valor " + str(x) + ": "))

    contador += 1

    if contador >= 6:
        suma += num
        cont += 1

print("La suma de los ultimos 5 valores ingresados es ", suma)
print("Se sumaron los ultimos ", cont, " numeros ingresados")