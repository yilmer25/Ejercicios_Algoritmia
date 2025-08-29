#Programa para obtener iniciales en mayusculas

#Entradas
#   Variable Entrada ,
#   Variable Salida

#Pedir Nombre y apellido

nombre=input(" ingresa tu nombre: ")
apellido=input(" ingresa Tu apellido: ")
Edad=input("Ingresa tu edad: ")
#Tomar la primera letra de cada uno y ponerla en mayusculas
iniciales= nombre[0].upper() + apellido[0].upper()
#mostrar resultados
print("Tus iniciales son: ", iniciales)
print("Tus nombres completos son", nombre.upper(),apellido.upper())
print("Tu edad es",Edad)


