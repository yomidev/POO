with open("frases.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    
cantidad = len(contenido)
print(f"El archivo tiene {cantidad} caracteres.")

nombre = input("Ingresa el nombre del archivo a copiar: ")
try:
    with open(nombre, "r", encoding="utf-8") as original:
        contenido = original.read()
    
    nuevo_nombre = f"copia_{nombre}"
    
    with open(nuevo_nombre, "w", encoding="utf-8") as copia:
        copia.write(contenido)
    print("Copia creada exitosamente")
    
except FileNotFoundError:
    print("El archivo no existe.")