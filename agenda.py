from datetime import datetime

class Agenda:
    def __init__(self):
        self.contactos = []
        
    def agregar_contacto(self, nombre, telefono, correo):
        contacto = {
            "nombre" : nombre.title(),
            "telefono": telefono,
            "correo" : correo.lower(),
            "fecha_registro" : datetime.now()
        }
        self.contactos.append(contacto)
        print(f"Contacto: {nombre} fue agregado correctamente")
        
    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos registrados")
        else:
            print("\n Lista de Contactos:")
            for c in self.contactos:
                print(f"-{c['nombre']} // Tel: {c['telefono']} // Correo: {c['correo']} // Fecha de Registro: {c['fecha_registro']}")
                
    def buscar_contacto(self, nombre):
        encontrados = [c for c in self.contactos if c["nombre"].lower() == nombre.lower()]
        if encontrados:
            for c in encontrados:
                print(f"Econtrado: {c['nombre']} // {c['telefono']} // {c['correo']} // {c['fecha_registro']}")
        else:
            print("No se econtro ningun contacto")
            
    def eliminar_contacto(self, nombre):
        for c in self.contactos:
            if c["nombre"].lower() == nombre.lower():
                self.contactos.remove(c)
                print("El contacto fue eliminado")
                return
        print("No se encontro el contacto")
        
agenda = Agenda()
agenda.agregar_contacto("Juanito", "5555555555", "juanito@gmail.com")
agenda.agregar_contacto("Carlos", "1234567890", "carlos@hotmail.com")

agenda.listar_contactos()
agenda.buscar_contacto("juanito")
agenda.eliminar_contacto("carlos")
agenda.listar_contactos()
    