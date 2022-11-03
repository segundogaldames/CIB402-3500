email = input("Ingrese un email: ")
cantidad = 0
x = 0

while x < len(email):
    if email[x] == "@":
        cantidad += 1

    x+=1

if cantidad == 1:
    print("El correo ingresado es correcto")
else:
    print("El correo ingresado es incorrecto")