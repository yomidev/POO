n = int(input("¿Cuantos registro deseas añadir?: "))

with open("estudiantes.txt", "w", encoding="utf-8") as archivo:
    for i in range(n):
        print(f"Estudiante {i+1}")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        edad = int(input("Edad: "))
        carrera = input("Carrera: ")
        semestre = int(input("Semestre: "))
        
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Apellidos: {apellidos}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Carrera:{carrera}\n")
        archivo.write(f"Semestre: {semestre}\n")
        archivo.write("-------------------\n")

print("Estudiantes guardados correctamente. Imprimiendo archivo: \n")

with open("estudiantes.txt","r", encoding="utf-8") as archivo:
    print(archivo.read())