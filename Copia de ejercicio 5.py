# 5. Determinar si un número es múltiplo de 5


# Parámetro de entrada:
#número entero ingresado por el usuario

#Proceso:
#el programa determina si el numero multiplo es de 5

#Parámetro de salida:
#Mensaje que indica si el número es múltiplo de 5 o no.

numero = int(input("Ingrese un número: "))
if numero % 5 == 0:
    print("El número es múltiplo de 5")
else:
    print("El número no es múltiplo de 5")