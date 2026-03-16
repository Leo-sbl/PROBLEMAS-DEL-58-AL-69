#PROBLEMA 69
def email_valido(email):
    return "@" in email

direccion = input("Ingrese su dirección de correo electrónico: ")

if email_valido(direccion):
    print("La dirección de correo es válida.")
else:
    print("La dirección de correo no es válida.")
