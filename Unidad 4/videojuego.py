class Personaje:
    
    def __init__(self, nombre, nivel, salud):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
        
    def atacar(self):
        print(f"{self.nombre} realiza un ataque básico.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Nivel: {self.nivel}, Salud: {self.salud}")
        
    def recibir_dano(self, cantidad):
        self.salud -= cantidad
        if self.salud <= 0:
            self.salud = 0
            print(f"{self.nombre} ha sido derrotado.")
        else:
            print(f"{self.nombre} recibe {cantidad} de daño. Salud restante: {self.salud}")
            
class Guerrero(Personaje):
    
    def __init__(self, nombre, nivel, salud, fuerza):
        super().__init__(nombre, nivel, salud)
        self.fuerza = fuerza
        
    def atacar(self):
        print(f"{self.nombre} ataca con una espada, causando {self.fuerza * 2} de daño.")
        
class Mago(Personaje):
    
    def __init__(self, nombre, nivel, salud, magia):
        super().__init__(nombre, nivel, salud)
        self.magia = magia
        
    def atacar(self):
        if self.magia >=10:
           print(f"{self.nombre} lanza un hechizo, causando {self.magia * 3} de daño.") 
           self.magia -= 10

        else:
            print(f"{self.nombre} no tiene suficiente magia para lanzar un hechizo.")
            print(f"Magia restante: {self.magia}")
    
    def curar(self):
        if self.magia >=5:
            self.salud += 20
            self.magia -= 5
            print(f"{self.nombre} se cura, salud actual: {self.salud}, magia restante: {self.magia}")
        else:
            print(f"{self.nombre} no tiene suficiente magia para curarse.")
            print(f"Magia restante: {self.magia}")
        
class Arquero(Personaje):
    
    def __init__(self, nombre, nivel, salud, flechas):
        super().__init__(nombre, nivel, salud)
        self.flechas = flechas

    def atacar(self):
        if self.flechas > 0:
            print(f"{self.nombre} dispara una flecha, causando {self.nivel * 2} de daño.")
            self.flechas -= 1
        else:
            print(f"{self.nombre} no tiene flechas para disparar.")
            print(f"Flechas restantes: {self.flechas}")
            
    def recargar(self, cantidad):
        self.flechas += cantidad
        print(f"{self.nombre} recarga {cantidad} flechas. Flechas actuales: {self.flechas}")
        
def main():
    print("=== Simulador de Personajes ===")
    print("1. Crear Guerrero")
    print("2. Crear Mago")
    print("3. Crear Arquero")
    
    opcion = input("Seleccione una opción (1-3): ")
    nombre = input("Ingrese el nombre del personaje: ")
    nivel = int(input("Ingrese el nivel del personaje: "))
    salud = int(input("Ingrese la salud del personaje: "))
    
    if opcion == "1":
        fuerza = int(input("Fuerza del guerrero: "))
        personaje = Guerrero(nombre, nivel, salud, fuerza)
    elif opcion == "2":
        magia = int(input("Cantidad de magia: "))
        personaje = Mago(nombre, nivel, salud, magia)
    elif opcion == "3":
        flechas = int(input("Cantidad de flechas: "))
        personaje = Arquero(nombre, nivel, salud, flechas)
    else: 
        print("Opción no valida")
        return
    
    print("\n--- Información del personaje creado ---")
    personaje.mostrar_info()
    
    print("\n--- Simulación de acciones ---")
    personaje.atacar()
    personaje.recibir_dano(30)
    
    if isinstance(personaje, Mago):
        personaje.curar()
    elif isinstance(personaje, Arquero):
        personaje.recargar(5)
    
main()
    