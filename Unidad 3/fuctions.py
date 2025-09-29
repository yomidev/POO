class Persona:
    
    def __init__(self):
        pass
    
    def saludar(self,nombre):
        print("Hola, ¿cómo estás?", nombre)
        
p = Persona
nombre = input("Ingresa tu nombre")
p.saludar("",nombre)