def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def mejor_calificacion(alumnos):
    mejor = None
    calificacion_max = -1
    for alumno in alumnos:
        max_alumno = max(alumno.calificaciones)
        if max_alumno > calificacion_max:
            calificacion_max = max_alumno
            mejor = alumno.nombre
    return mejor, calificacion_max