print ("Registre usuario y contraseña")
usuario0 = input()
contraseña0 = input()
intentos =3
print ("Introduzca su usuario y contraseña")
while intentos > 0:
        print("Usuario")
        usuario = input()
        contraseña = input()
        if usuario == usuario0 and contraseña == contraseña0:
            print("Acceso concedido")
        else:
                intentos -= 1
                if intentos > 0:
                    print("El nombre de usuario o contraseña no es correcto")
                else:
                    print("Se ha bloqueado el acceso al haberse dado demasiados intentos")

