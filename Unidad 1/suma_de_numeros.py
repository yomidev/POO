suma = 0
contador = 1
num = int(input("Ingresa un numero (para terminar ingresa 0): "))

while num != 0:
    suma = suma+num
    num = int(input("Ingresa un numero (para terminar ingresa 0): "))
    contador = contador + 1
    
print("La suma total de ", contador," numero(s) es: ",suma)