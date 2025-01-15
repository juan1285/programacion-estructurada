#en este ejercicio vamos a validar un usuario y contraseña del usuario 
#si el usuario es correcto y la contraseña es correcta
#entonces se imprime un mensaje de bienvenida 



# se pide al usuario que ingrese un usuario 
usuario = input("ingrese su usuario: ")

# se pide al usuario que ingrese su contraseña
contraseña = input("ingrese su contraseña: ")

#se valida si el usuario es igual a "admin"ny la contraseña es igual a "admin123"
if usuario == "admin" and contraseña == "admin123":
    print("bienvenido al sistema")
else:
    print("usuario o contraseña incorrecta")