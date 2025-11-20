def sistema_de_calificaciones():
    print("\n---Sistema de Calificaciones---")
    
    #Define la longuitud que tendra la matriz Ej. (4,3)
    estudiantes = int(input("Ingrese el numero de estudiantes a capturar: "))
    materias = int(input("Ingrese el numero de materias a capturar: "))
    
    #Crear matriz
    calificaciones = []
    for i in range(estudiantes):
        fila = []
        print(f"Ingresa las calificaciones del estudiante {i+1}")
        for j in range(materias):
            cal = float(input(f"Calificación de la materia {j+1}: "))
            fila.append(cal)
        calificaciones.append(fila)
        
    #Promedio de estudiante
    print("\n Promedio por estudiante")
    for i in range(estudiantes):
        promedio = sum(calificaciones[i])/materias
        print(f"El promedio del estudiante {i+1} es : {promedio:.2f}")
    
    #Promedio de materias
    print("\n---Promedio por materia")
    for j in range(materias):
        suma = 0
        for i in range(estudiantes):
            suma += calificaciones[i][j]
        promedio = suma/estudiantes
        print(f"La calificacion de la materia {j+1} es: {promedio:.2f}")
        
    #Calificacion mas alta y baja
    total = [cal for fila in calificaciones for cal in fila]
    calificacion_alta = max(total)
    calificacion_baja = min(total)
    
    print("Estadisticas generales")
    print(f"La calificacion mas alta es: {calificacion_alta}")
    print(f"La calificacion mas baja es: {calificacion_baja}")

sistema_de_calificaciones()