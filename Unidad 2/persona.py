class Persona:
    especie = "Humano"
    def __init__(self, nombre, edad, curp, nacionalidad, huellas_digitales, num_ine, escolaridad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.curp = curp
        self.nacionalidad = nacionalidad
        self.huellas_digitales = huellas_digitales
        self.num_ine = num_ine
        self.escolaridad = escolaridad
        self.telefono = telefono
    
    def saludar(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} años, mi numero de telefono es: {self.telefono} y soy un {Persona.especie}")
        
persona1 = Persona("Anita",25,"AAAA010101MASSRM02","Mexicana","00000", "1234567890","Preparatoria", "+52 1 55 5555 5555")
persona2 = Persona("Carlitos",38,"CAAA010101MASSRM01","Chileno","0000","012919231","Maestría","+561098765432")

persona1.saludar()
persona2.saludar()