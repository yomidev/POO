#---Matriz---
matriz = [
    list("p y t h o n a b c d".split()),
    list("x p y t h o n e f g".split()),
    list("h x p y t h o n i j".split()),
    list("o h x p y t h o h k".split()),
    list("t o h x p y t h o l".split()),
    list("y t o h x p y t h m".split()),
    list("n y t h o n p y t h".split()),
    list("a b c d e f g h i j".split()),
]

palabra = "python"
filas = len(matriz)
columna = len(matriz[0])

#Direcciones
direcciones = [
    (0, 1), #derecha
    (0, -1), #izquierda
    (1, 0), #arriba
    (-1, 0), #abajo
    (1, 1), #diagonal hacia abajo del lado derecho
    (1, -1), #diagonal hacia abajo del lado izquierdo
    (-1, 1), #diagonal hacia arriba del lado derecho
    (-1, -1) #diagonal hacia arriba del lado izquierdo
]

def buscar_palabra(f, c, palabra):
    posiciones = []
    for df, dc in direcciones:
        temporal = []
        ff, cc = f, c
        for letra in palabra:
            if 0 <= ff < filas and 0 <= cc < columna and matriz[ff][cc] == letra:
                temporal.append((ff,cc))
            else:
                break
            ff += df
            cc += dc
        if len(temporal) == len(palabra):
            posiciones.append(temporal)
    return posiciones

coincidencias = []
for i in range(filas):
    for c in range(columna):
        if matriz[i][c] == palabra[0]:
            resultado = buscar_palabra(i, c, palabra)
            if resultado:
                coincidencias.extend(resultado)

marcada = [filas.copy() for filas in matriz]
for lista_pos in coincidencias:
    for (f, c) in lista_pos:
        marcada[f][c] = marcada[f][c].upper()

print("Resultado")
for fila in marcada:
    print(" ".join(fila))