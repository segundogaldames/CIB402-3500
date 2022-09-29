#programa que calcula la superficie de un cuadrado
#solicitar el ingreso del valor de un lado
lado = input("Ingrese el valor de un lado: ")

#transformamos el dato recibido en un entero
#la funcion input recibe un dato de tipo caracter o string
lado = int(lado)

#calcular la superficie del cuadrado
superficie = lado * lado

#mostramos el resultado
print("La superficie del cuadrado es: ", superficie)