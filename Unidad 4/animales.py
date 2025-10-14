class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        print("El animal hace un sonido")
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato maulla")
        
perro = Perro("Solovino", 4)
gato = Gato("Manchas", 6)

perro.presentarse()
perro.hacer_sonido()
gato.presentarse()
gato.hacer_sonido()