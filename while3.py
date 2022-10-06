contador = 1
suma = 0

while contador <= 5:
    num = int(input("Ingrese el valor " + str(contador) + ": "))
    suma += num # suma = suma + num
    contador += 1

print("La suma de los valores ingresados es: ", suma)
