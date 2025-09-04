import random

secreto = random.randint(1,30)
intentos = 0
adivinar = 0

while adivinar != secreto:
    adivinar = int(input("Adivina el numero (1 - 30):"))
    intentos = intentos + 1
    if adivinar < secreto:
        print("El numero a adivinar es mayor")
    elif adivinar > secreto:
        print("El numero a adivinar es menor")
    else:
        print("Correcto, tardaste ",intentos," intentos")