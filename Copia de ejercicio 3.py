# 3. Identificar si un estudiante aprobó o reprobó

#Parámetro de entrada:
#nota -> número decimal ingresado por el usuario que representa la calificación del estudiante

#Proceso:
#Solicita la nota del estudiante.
#Verifica si la nota es mayor o igual a 60.
#Si es así, indica que aprobó, de lo contrario, indica que reprobó.

#Parámetro de salida:
#Mensaje que indica si el estudiante aprobó o reprobó.

nota = float(input("Ingrese la nota del estudiante: "))
if nota >= 60:
    print("El estudiante aprobó")
else:
    print("El estudiante reprobó")