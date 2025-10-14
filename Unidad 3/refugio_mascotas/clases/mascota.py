class Mascota:
    
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        print(f"Mascota registrada: {self.nombre} , especie: {self.especie}")
    
    def __del__(self):
        print(f"La mascota {self.nombre} ha sido adoptada. Buena suerte!")
    
    def saludar(self, persona=None):
        if persona:
            print(f"{self.nombre} saluda a {persona}")
        else:
            print(f"{self.nombre} te saluda felizmente")
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre} / Edad: {self.edad} / Especie: {self.especie}")
    
    def edad_humano(self):
        if self.especie.lower() == "perro":
            return self.edad*7
        elif self.especie.lower() == "gato":
            return self.edad*5
        else:
            return self.edad