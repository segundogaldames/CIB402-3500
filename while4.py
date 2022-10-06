cantidad = 0
contador = 1

num = int(input("Ingrese la cantidad de perfiles: "))

while contador <= num:
    largo = float(input("Ingrese el largo del perfil " + str(contador) + ": "))

    if largo > 1.2 and largo < 1.3:
        cantidad += 1

    contador += 1

print("El numero de perfiles que cumple con el largo es: ", cantidad)