frases = []
n_frases = int(input("Ingrese el numero de frases a guardar: "))

for i in range(n_frases):
    frase = input(f"Frase {i+1}: ")
    frases.append(frase)
    
#Guardar en archivo
with open("frases.txt", "w", encoding="utf-8") as archivo:
    for frase in frases:
        archivo.write(frase + "\n")
    
#Leer
print("\n Contenido del archivo 'frases.txt': ")
with open("frases.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.readlines()

for linea in contenido:
    print(linea.strip())
    
print(f"\nNúmero total de frases: {len(contenido)}")
print("\n Frases guardadas correctamente")
archivo.close()