num1 = int(input("Ingrese el primer valor: "))

num2 = int(input("Ingrese el segundo valor: "))


if num1 > num2:
    suma = num1 + num2
    resta = num1 - num2
    print("La suma de los valores es: ", suma)
    print("La diferencia de los valores es: ", resta)
else:
    producto = num1 * num2
    division = num1 / num2
    print("El producto de los valores es: ", producto)
    print("El cuociente de los valores es: ", division)