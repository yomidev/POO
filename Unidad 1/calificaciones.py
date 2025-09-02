#cal1 = float(input("Ingresa la primer calificación: "))
#cal2 = float(input("Ingresa la segunda calificación: "))
#cal3 = float(input("Ingresa la tercer calificación: "))
#cal4 = float(input("Ingresa la cuarta calificación: "))
#cal5 = float(input("Ingresa la quinta calificación: "))

#promedio = (cal1+cal2+cal3+cal4+cal5)/5

#print("El promedio es: ",promedio)

calificaciones = []
for i in range(5):
    cal = float(input(f"Ingresa tu calificación {i+1}: "))
    calificaciones.append(cal)
    
promedio = sum(calificaciones)/len(calificaciones)
print("El promedio es: ", promedio)

if promedio >=70:
    print("Aprobado")
else:
    print("Reprobado")
    