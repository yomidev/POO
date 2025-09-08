class Coche:
    def __init__(self,color,marca,modelo,tipo_motor,tipo_transmision,numero_llantas,numero_asientos,cilindros,numero_espejos):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.tipo_motor = tipo_motor
        self.tipo_transmision = tipo_transmision
        self.numero_llantas = numero_llantas
        self.numero_espejos = numero_espejos
        self.cilindros = cilindros
        self.numero_asientos = numero_asientos
        
    def avanzar(self):
        print("El coche esta avanzando")
    def frenar(self):
        print("El coche esta frenando")
    def encender(self):
        print("El coche esta encendiendo")
    def reversa(self):
        print("el coche esta avanzando de reversa")
    def abrir_puertas(self):
        print("El coche esta abriendo las puertas")
    def encender_luces(self):
        print("El coche esta encendiendo las luces")
    def abrir_cajuela(self):
        print("El coche esta abriendo la cajuela")

#Objeto

mi_coche = Coche("Verde","Honda","Civic","x","Automatico",4,4,4,3)
print("Tu coche es un ",mi_coche.marca," ",mi_coche.modelo," color ",mi_coche.color)
mi_coche.encender()
mi_coche.avanzar()