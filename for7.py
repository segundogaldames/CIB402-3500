from opcode import hascompare


turno_am = 0
turno_tarde = 0
turno_noche = 0
suma = 0

input("ingrese las edades de los estudiantes del turno de mañana: ")

for x in range(1, 6):
    edad = int(input("Ingrese la edad " + str(x) + ": "))
    suma += edad

turno_am = suma/5

input("ingrese las edades de los estudiantes del turno de tarde: ")

for x in range(1, 7):
    edad = int(input("Ingrese la edad " + str(x) + ": "))
    suma += edad

turno_tarde = suma/6

input("ingrese las edades de los estudiantes del turno de noche: ")

for x in range(1, 12):
    edad = int(input("Ingrese la edad " + str(x) + ": "))
    suma += edad

turno_noche = suma/11

print("El promedio de los alumnos de mañana es ", turno_am)
print("El promedio de los alumnos de tarde es ", turno_tarde)
print("El promedio de los alumnos de noche es ", turno_noche)

#cual de los tres turnos tiene edad promedio mayor

if turno_am > turno_tarde and turno_am > turno_noche:
    print("El turno de mayor edad promedio es el turno de mañana")
else:
    if turno_tarde > turno_noche:
        print("El turno de mayor edad promedio es el turno de tarde")
    else:
        print("El turno de mayor edad promedio es el turno de noche")

# Este software sirve para hacer
# ingreso de promedios por
# alumnos segun turno