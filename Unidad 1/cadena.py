texto = input("Ingresa un texto: ")
vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vocales:
        contador = contador + 1
        
print("El numero de vocales encontrado es: ",contador)