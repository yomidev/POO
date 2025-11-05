from animales.animal import Animal

class Perro(Animal):
    def __init__(self, name, edad, raza):
        super().__init__(name, edad)
        self.raza = raza
    
    def hablar(self):
        return f"{self.name} esta ladrando"
    def moverse(self):
        return f"{self.name} corre moviendo la cola"
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} // Es un perro de raza {self.raza}"