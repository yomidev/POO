from animales.animal import Animal

class Gato(Animal):
    def __init__(self, name, edad, color):
        super().__init__(name, edad)
        self.color = color
        
    def hablar(self):
        return f"{self.name} esta maullando"
    def moverse(self):
        return f"{self.name} se mueve sigilosamente"
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} // Es un gato de color {self.color}"