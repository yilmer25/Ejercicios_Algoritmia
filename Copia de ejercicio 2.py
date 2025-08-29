# 2. Comprobar si un año es bisiesto

# Parámetro de entrada:
#   año -> número entero que representa el año ingresado por el usuario

# Proceso:
#  el programa determina si  el año es bisiesto o no.

# Parámetro de salida:
#   Mensaje por pantalla que indica si el año es bisiesto o no.

año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")