# 1. Determinar si un número es negativo

# Parámetro de entrada:
# numero -> número entero ingresado por el usuario

# Proceso:
#  Solicita al usuario un número entero.
#  Verifica si el número es menor que cero.
#  Dependiendo del resultado, muestra un mensaje indicando si es negativo o no.


# Parámetro de salida:
#   Mensaje por pantalla indicando si el número es negativo o no.

numero = int(input("Ingrese un número: "))
if numero < 0:
    print("El número es negativo")
else:
    print("El número no es negativo")