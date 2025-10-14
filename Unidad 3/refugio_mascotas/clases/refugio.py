from clases.mascota import Mascota

class Refugio:
    total_mascotas = 0
    
    def __init__(self):
        self.mascotas = []
    
    def registrar_mascotas(self):
        nombre = input("Ingrese el nombre de la mascota: ")
        especie = input("Ingrese la especie de la mascota: ")
        edad = int(input("Ingrese la edad: "))
        nueva = Mascota(nombre, especie, edad)
        self.mascotas.append(nueva)
        Refugio.total_mascotas = Refugio.total_mascotas+1
        
    def mostrar_mascotas(self):
        if not self.mascotas:
            print("No hay mascotas registradas")
        else:
            for m in self.mascotas:
                m.mostrar_info()
    def adoptar(self):
        nombre = input("Ingresa el nombre de la mascota a adoptar: ")
        for m in self.mascotas:
            if m.nombre.lower() == nombre.lower():
                self.mascotas.remove(m)
                Refugio.total_mascotas -= 1
                del m
                break
            else:
                print("Mascota no encontrada")
                
    @classmethod
    def mostrar_total(cls):
        print(f"Total de mascotas registradas: {cls.total_mascotas}")