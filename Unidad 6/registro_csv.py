import os

archivo = "estudiantes.csv"
existe = os.path.isfile(archivo)

n = int(input("¿Cuántos estudiantes deseas registrar?: "))

with open(archivo, "a", encoding="utf-8") as csv:
    if not existe:
        csv.write("nombre,apellidos,edad,carrera,semestre\n")
        
    for i in range(n):
        print(f"Estudiante # {i+1}")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        edad = int(input("Edad: "))
        carrera = input("Carrera: ")
        semestre = int(input("Semestre: "))
        
        csv.write(f"{nombre},{apellidos},{edad},{carrera},{semestre}\n")
print("Datos guardados correctamente")