pwd = "mimamamemima"

while True:
    password = input("Ingresa la contraseña: ")
    if password == pwd:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta, intenta de nuevo")