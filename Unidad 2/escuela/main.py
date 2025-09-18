from funciones.alumnos import Alumno
from funciones.promedios import calcular_promedio, mejor_calificacion

#Crear lista de alumnos
alumnos = [
    Alumno("Juan", 20, [85, 90, 78]),
    Alumno("Maria", 22, [92, 88, 95]),
    Alumno("Luis", 19, [70, 75, 80])
]

#Listar alumnos
for alumno in alumnos:
    print(alumno)
    
#Calcular promedios de alumno en especifico
print("\nPromedio de Luis:", calcular_promedio(alumnos[2].calificaciones))

#Calcular mejor calificacion entre todos los alumnos
mejor, calificacion = mejor_calificacion(alumnos)
print(f"\nMejor calificacion es de {mejor} con una calificacion de {calificacion}")