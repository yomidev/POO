from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, edad):
        self.name = name
        self.edad = edad
        
    @abstractmethod
    def hablar(self):
        pass
    @abstractmethod
    def moverse(self):
        pass
    
    def mostrar_informacion(self):
        return f"Nombre: {self.name} // Edad {self.edad} años"