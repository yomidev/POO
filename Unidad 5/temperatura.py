def leer_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            valor = float(input(f"Ingrese la temperatura en ({f},{c}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{elem:5}" for elem in fila))
    
def matriz_calor(matriz, promedio):
    nueva = []
    for fila in matriz:
        nueva_fila = []
        for elem in fila:
            if elem > promedio:
                nueva_fila.append("🔥/alto")
            elif elem < promedio:
                nueva_fila.append("❄️/bajo")
            else:
                nueva_fila.append("🌡️/normal")
        nueva.append(nueva_fila)
    return nueva

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

matriz = leer_matriz(filas, columnas)

#Buscar min y max
maximo = matriz[0][0]
minimo = matriz[0][0]
pos_max = (0,0)
pos_min = (0,0)

suma = 0
contador = 0

for f in range(filas):
    for c in range(columnas):
        valor = matriz[f][c]
        suma = suma + valor
        contador = contador + 1
        if valor > maximo:
            maximo = valor
            pos_max = (f,c)
        if valor < minimo:
            minimo = valor
            pos_min = (f,c)

promedio = suma/contador

print("\n Matriz Ingresada: ")
imprimir_matriz(matriz)
print(f"\n Temperatura Maxima: {maximo} en {pos_max}")
print(f"\n Temperatura Minima: {minimo} en {pos_min}")
print(f"\n Promedio: {promedio}")
print("\n Matriz de Calor: ")
imprimir_matriz(matriz_calor(matriz, promedio)
)