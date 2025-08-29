def numero_rango():
    numero = int(input("Ingrese un número: "))
    if numero > 100 or numero < -100:
        print("El número cumple la condición")
    else:
        print("El número no cumple la condición")
numero_rango()