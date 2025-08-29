# 7. Determinar tipo de triángulo
a = float(input("Ingrese el lado 1: "))
b = float(input("Ingrese el lado 2: "))
c = float(input("Ingrese el lado 3: "))
if a == b == c:
    print("El triángulo es equilátero")
elif a == b or b == c or a == c:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")