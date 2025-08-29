# 4. Verificar si una persona puede votar

#Parámetros de entrada:
#Edad:número entero ingresado por el usuario que representa la edad de la persona
#Nacionalidad  ingresada por el usuario representa la nacionalidad de la persona

#Proceso:
#Solicita la edad y la nacionalidad..
#Verifica si la persona tiene 18 años o más y es colombiana.
#Si cumple ambas condiciones, puede votar, si no, no puede votar.

#Parámetro de salida:
#Mensaje que indica si la persona puede votar o no.

edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")
if edad >= 18 and nacionalidad.lower() == "colombiana":
    print("Puede votar")
else:
    print("No puede votar")