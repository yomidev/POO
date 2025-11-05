from animales.animal import Animal

class Loro(Animal):
    def __init__(self, name, edad, puede_hablar):
        super().__init__(name, edad)
        self.puede_hablar = puede_hablar
        
    def hablar(self):
        if self.puede_hablar:
            return f"{self.name} dice: ¡Hola!"
        else:
            return f"{self.name} emite sonidos extraños"
        
    def moverse(self):
        return f"{self.name} esta volando"
    
    def mostrar_informacion(self):
        habla = "si" if self.puede_hablar else habla= "no"
        return f"{super.mostrar_informacion()} // Puede hablar: {habla}"