class Estudiante:
    
    lista_estudiantes = []
    
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
        Estudiante.lista_estudiantes.append(self)
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Calificación: {self.calificacion}")
    
    @classmethod
    def total_estudiantes(cls):
        return len(cls.lista_estudiantes)
    
    @classmethod
    def promedio_general(cls):
        if len(cls.lista_estudiantes) == 0:
            return 0
        else:
            total= sum([est.calificacion for est in cls.lista_estudiantes])
            return total/len(cls.lista_estudiantes)
        
        
print("Registro de Estudiantes")
num_estudiantes = int(input("¿Cuántos estudiantes desea registrar?:"))

for i in range(num_estudiantes):
    nombre = input(f"Nombre del estudiantes {i+1}: ")
    calificacion = float(input(f"Calificación final de {nombre}:"))
    Estudiante(nombre, calificacion)
    
print("\n--- Lista de Estudiantes registrados ---")
for est in Estudiante.lista_estudiantes:
    est.mostrar_info()
    
print("\n--- Resumen ---")
print(f"Número de estudiantes registrados : {Estudiante.total_estudiantes()}")
print(f"Promedio General de estudiantes: {Estudiante.promedio_general():.2f}")