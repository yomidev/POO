secreto = 18

while True:
    intento = int(input("Adivina el numero: "))
    if intento == secreto:
        print("Acertaste")
        break
    else:
        print("Intenta de nuevo")
    