class Alumno:
    def __init__(self, nombre, edad, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Calificaciones: {self.calificaciones}"