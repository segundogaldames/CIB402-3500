suma = 0

for f in range(10):
    num = int(input("Ingrese el valor " + (f+1) + ": "))
    suma += num  # suma = suma + num

promedio = suma /10

print("La suma de los valores ingresados es: " + suma)
print("El promedio es: " + promedio)