n = int(input("Ingresa un numero: "))
suma = 0

#for i in range(1,n+1):
    #if (i%2 == 0):
        #suma=suma+i

for i in range(2,n+1,2):
    suma = suma+i

print("La suma de los numeros pares de 0 hasta ",n," es: ",suma)