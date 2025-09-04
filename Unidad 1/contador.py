num = int(input("Ingresa un numero: "))
while num == 0:
    print("No puedes ingresar el numero 0")
    num = int(input("Ingresa un numero: "))

while num > 0:
    print(num)
    num = num-1