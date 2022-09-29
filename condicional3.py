contador = 1
suma = 0

while(contador <= 3):
    nota = float(input("Ingrese la nota " + str(contador) + ": "))

    while nota < 1.0 or nota > 7.0:
        print("La nota no es valida")
        nota = float(input("Ingrese la nota " + str(contador) + ": "))

    suma = suma + nota
    contador = contador + 1

promedio = suma / 3

print("El promedio es: ", promedio)

if promedio >= 5:
    print("Aprobado con excelencia")
else:
    if promedio >= 4:
        print("Aprobado con promedio regular")
    else:
        print("Reprobado")

