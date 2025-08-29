def permiso_codigo():
    codigo = int(input("Ingrese el código de administrador: "))
    if codigo == 12345:
        print("Acceso concedido")
    else:
        print("Acceso denegado")
permiso_codigo()