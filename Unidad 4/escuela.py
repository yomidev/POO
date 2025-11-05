class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_informacion(self):
        return print(f"Nombre: {self.nombre}, Edad: {self.edad}")
    
    def presentarse(self):
        return print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    
class Estudiante(Persona):
    
    def __init__(self, nombre, edad, matricula, carrera):
        super().__init__(nombre, edad)
        self.matricula = matricula
        self.carrera = carrera
        self.promedio = 0.0
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Matrícula: {self.matricula}, Carrera: {self.carrera}, Promedio: {self.promedio}")
    
    def actualizar_promedio(self, nuevo_promedio):
        self.promedio = nuevo_promedio
        print(f"El nuevo promedio de {self.nombre} es {self.promedio}")
    
class Profesor(Persona):
    
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Materia que imparte: {self.materia}")
        
    def calificar(self, estudiante, calificacion):
        estudiante.actualizar_promedio(calificacion)
        print(f"{self.nombre} ha calificado a {estudiante.nombre} con {calificacion}")
        
class Administrativo(Persona):
    
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Puesto: {self.puesto}")

    def registrar_estudiante(self, nombre, edad, matricula, carrera):
        print(f"{self.nombre} ha registrado al estudiante {nombre}.")
        return Estudiante(nombre, edad, matricula, carrera)
    
def main():
    print("=== Sistema de Control Escolar ===")
    admin = Administrativo("Ana Pérez", 45, "Secretaria")
    profesor = Profesor("Carlos López", 38, "Matemáticas")
    
    # Registrar un estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    matricula = input("Ingrese la matrícula del estudiante: ")
    carrera = input("Ingrese la carrera del estudiante: ")
    
    estudiante = admin.registrar_estudiante(nombre, edad, matricula, carrera)
    
    print("\n--- Información de las personas ---")
    admin.mostrar_informacion()
    profesor.mostrar_informacion()
    estudiante.mostrar_informacion()
    
    print("\n--- Presentaciones ---")
    admin.presentarse()
    profesor.presentarse()
    estudiante.presentarse()
    
    print("\n--- Calificación del estudiante ---")
    calificacion = float(input(f"Ingrese la calificación para {estudiante.nombre}: "))
    profesor.calificar(estudiante, calificacion)
    
    print("\n--- Información actualizada del estudiante ---")
    estudiante.mostrar_informacion()
    
if __name__ == "__main__":
    main()